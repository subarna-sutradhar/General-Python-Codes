def findlength():
    name=input("enter your name\t")
    ctr=0
    for i in name:
        ctr+=1
    for j in name:
        print(j,end=" ")
    print("length of the name is {}".format(ctr))