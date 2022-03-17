def seg(str):
    
    low_list=[]
    upp_list=[]

    for i in str:
        if i.islower()==True:
            low_list.append(i)
        elif i.isupper()==True:
            upp_list.append(i)
    print("Uppercase list: ",upp_list)
    print("lowercase list: ",low_list)