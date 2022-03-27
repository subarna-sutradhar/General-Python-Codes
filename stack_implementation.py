"""Stack implementation"""
l=[]
c="y"
while c=="y":
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    choice=int(input("Enter the choice: "))
    if choice==1:
        a=int(input("Enter the no: "))
        l.append(a)
    elif choice==2:
        if l==[]:
            print("Empty Stack")
        else:
            a=int(input("Enter the number"))
            l.pop(a)
    elif choice==3:
        print(l)
    else:
        print("Wrong input")
    c=input("Continue? ")