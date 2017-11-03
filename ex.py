
import os
fsize=os.path.getsize("mft")
cnt=0

f=open("mft","rb")

while fsize:
    s=f.read(1)
 
    if s == '':
        break
    

#80 to 88 time print
    if cnt == 80:
        for i in range(0,8):
            print "%02x" % int(ord(s)),
            cnt=cnt+1
            fsize=fsize-1
            s=f.read(1)
        print ""
    cnt=cnt+1
    if cnt == 1024:
        cnt=0
        

f.close()
