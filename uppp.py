def addtolist(str):
    upc=[]
    lwc=[]
    for i in str:
        if(i.isupper()==True):
            upc.append(i)
        elif(i.islower()==True):
            lwc.append(i)
    print(upc)
    print(lwc)