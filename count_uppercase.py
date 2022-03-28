import os
spcfile=input("Enter a file name ")
wc=0
if os.path.exists(spcfile):
    print("File already exists")
    spc=open(spcfile)
    print(spc.read())
    with open(spcfile,'r') as f:
        for line in f:
            words=line.split()
            for i in words:
                if i[0].isupper()==True:
                    print(i)
                    wc+=1
        print("Total number of uppercase words ",wc)