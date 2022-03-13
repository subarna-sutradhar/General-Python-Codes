#using class
class stack:
    s = []
    def push(self):
        a = int(input("Enter any number: "))
        stack.s.append(a)
        print(stack.s)

    def display(self):  #this is not needed if we use print(stack.s)
        L = len(stack.s)
        for i in range(L - 1, -1, -1):
            print(stack.s[i])

obs = stack()
ans = input("Enter y to continue: ")
ch = 0
while(ans =="y"):
    print("1.Push")
    print("2.Pop")
    print("3.Display")  #can be neglected if used print(stack.s)
    ch = int(input("Enter your selection: "))
    if(ch == 1):
        obs.push()
        #obs.display
    elif(ch == 2):
        if(obs.s == []):
            print("STACK IS EMPTY")

        else:
            obs.s.pop()
            #obs.display()

    elif(ch == 3):
        print("TOU HAVE OPTED FOR 3")
        obs.display()
    ans = input("Enter y to continue: ")