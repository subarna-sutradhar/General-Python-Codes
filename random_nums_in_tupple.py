import random
"""a = random.randint(20,50) this is will be global
and print same num every time if given before the function"""
def tup():
    t1 = ()
    t2 = ()
    while(True):
        ans = input("Continue? ")
        a = random.randint(20,50)
        if ans == "y" or ans == "Y":
            t1 = (a,)
            t2 = t2 + t1
            print(t2)
        else:
            break
tup()