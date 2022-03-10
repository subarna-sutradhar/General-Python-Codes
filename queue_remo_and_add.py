mylist = [20, 30, 40, 50]
print(mylist)
ch = 0
ans = input("Enter y to continue: ")
while(ans == "y"):
    print("1 : Add in the queue")
    print("2 : Delete from the queue")
    
    ch = int(input("Enter the choice(1/2): "))
    if(ch == 1):
        val = int(input("Enter the nodal value: "))
        mylist.append(val)
        print(mylist)
            
    elif(ch == 2):
        mylist.remove(mylist[0])
        print(mylist)
    else:
        break
    ans = input("Enter y to continue: ")