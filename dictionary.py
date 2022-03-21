dict={}
ran=int(input("enter the range "))
for i in range(ran):
    name=input("enter the name: ")
    phone=int(input("enter the phone no: "))
    dict[name]=phone
print("Querry Begins")
qur=input("enter the name for details: ")
print(qur,"has the phone number: ",dict[qur])
while(True):
    a=input("search more? ")
    if(a=="Y" or a=="y"):
        b=input("enter the name for details: ")
        print(b,"has the phone number: ",dict[b])
    else:
        break