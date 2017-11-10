#-*- coding: utf-8 -*-
import os
import time

#global fsize
#global s

fsize = os.path.getsize("mft")
f=open("mft","rb")
j=0
cnt=0


def CreatedTime(s, cnt, fsize ):
    print "[*] Created Time : ",

    for i in range(0,8):
        print "%02x" % int(ord(s)),
        fsize=fsize-1
        s=f.read(1)
        cnt=cnt+1
    print ""
    return s 

if __name__ == "__main__":
    while fsize:
        s=f.read(1)
        cnt = cnt +1

        if cnt == 61: #file information size
            stsize=ord(s)
            stsize = stsize - 28 

        #if s == '':
        #    break

        if cnt == 81: # CreatedTime
            CreatedTime(s, cnt, fsize)
            cnt = cnt + 8

            f.read(stsize)
            f.read(83)
            cnt = cnt +stsize
            cnt = cnt + 83
             
            s=f.read(1) #<- filename length 
            cnt =cnt + 1
             
            print "[*] File Length : ",
            print binascii.b2a_hex('aaa')
            #print "%02x" % s
            length = int(s) 
              
            f.read(1)
            s=f.read(1)

           
            print "File Name : ",
            for i in range(0,length*2):
                print s,
                s=f.read(1)
                cnt = cnt + 1
            print ""

        if cnt == 1024: # Changed Entry
            print " MFT Entry Changed !!!"
            print ""
            time.sleep(1)
            cnt=0 

f.close()
