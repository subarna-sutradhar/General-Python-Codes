def repeating():
     abc=input("enter the name ")
     x=abc[3]
     ctr=0
     for i in abc:
          if(i==x):
                ctr+=1
     print("The no of times the 4th letter of your name repeatig is " + str(ctr))
