#without using class
"""stack"""
s = []
ans = input("Enter y to continue: ")
ch = 0
while(ans == "y"):
    print("1.Push: ")
    print("2.Pop: ")
    print("3.Display: ")
    ch = int(input("Enter your choice: "))
    if(ch == 1):
        a = int(input("Enter any number: "))
        s.append(a)
        print(s)
    elif(ch == 2):
        if(s == []):
            print("STACK IS EMPTY")
        else:
            print("Deleted element is: ",s.pop())

    elif(ch == 3):
        L = len(s)
        for i in range(L - 1, -1, -1):
            print(s[i])

    else:
        print("WRONG INPUT")
    ans = input("Enter y to continue: ")