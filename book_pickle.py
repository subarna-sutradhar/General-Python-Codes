import pickle
def createFile():
    while True:
        
        spcfile=open('Book.dat','ab')
        bno=int(input("Enter the Book Number: "))
        bname=input("Enter the Book Name: ")
        auth=input("Enter the Author: ")
        prc=int(input("Enter the Price: "))
        L=[bno,bname,auth,prc]
        pickle.dump(L,spcfile)
        ans=input('CONTINUE? ')
        if ans=='n' or ans=='N':
            break
    spcfile.close()
createFile()

def CountRec(auth):
    spcfile=open('Book.dat','rb')
    x=0
    try:
        while True:
            i=pickle.load(spcfile)
            if auth==i[2]:
                x+=1
    except EOFError:
        pass
    spcfile.close()
    print(auth,'has written ',x,' books')
CountRec('ABC')