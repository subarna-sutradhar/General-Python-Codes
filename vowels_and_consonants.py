def totalvc():
    name = input("Enter you name: ")
    ctrc = 0
    ctrv = 0
    for i in name:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            ctrc+=1
        else:
            ctrv+=1
    print("You name has {} number of vowels and {} number of consonants".format(ctrc,ctrv))

totalvc()