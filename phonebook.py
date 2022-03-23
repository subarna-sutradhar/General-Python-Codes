phbk=dict()
n=int(input("Enter total no of friends "))
i=1
while(i<=n):
    a=input("Enter name ")
    b=int(input("Enter number "))
    phbk[a]=b
    i=i+1
print("________MENU_________")
print("1: Search number")
print("2: Delete record")
print("3: Edit a record")
print("4. Quit")
user_answer=int(input("Enter 1,2,3 or 4"))
print()
if(user_answer==1):
    
    name=input("Enter name ")
    f=0
    l=phbk.keys()
    for j in l:
        if(j==name):
            print("Phone number = ",phbk[j])
            f=1
    if(f==0):
        print("Name does not exist")

    
elif(user_answer==2):
    
    name=input("Enter name ")
    del phbk[name]
    ll=phbk.keys()
    print("Updated Phonebook Information")
    print("Name",'\t',"Phone number")
    for i in ll:
        print(i,'\t',phbk[i])
        continue

elif(user_answer==3):
    name=input("Enter name ")
    f=0
    lll=phbk.keys()
    for j in lll:
        if(j==name):
            bb=int(input("Enter number "))
            phbk[j]=bb
            f=1
            print(phbk.items())
    if(f==0):
        print("Name does not exist")


else:
    quit()