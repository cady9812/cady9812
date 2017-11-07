
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
    time.sleep(2)
    return s 

if __name__ == "__main__":
    while fsize:
        s=f.read(1)
        cnt = cnt +1

        #if s == '':
        #    break

        if cnt == 81: # CreatedTime
            CreatedTime(s, cnt, fsize)
            cnt = cnt + 8
        

        if cnt == 241: # filename length 
            print "[*] File Name Length : ",
            print "%02x" % int(ord(s)),
            print ""
            flen=ord(s)
            s=f.read(1)
            cnt=cnt+2
            s=f.read(1)
#            print "File Name : ",
#            for i in range(0,flen):
#                time.sleep(3)
#                if s != '':
#                    print chr(ord(s)),
#                else:
#                    i = i - 1
#                s=f.read(1)
#                cnt = cnt + 1
#            print ""

        if cnt == 1024: # Changed Entry
            print " MFT Entry Changed !!!"
           
            print ""
            time.sleep(1)
            cnt=0 

f.close()
