"""ADD ASTRING IN A LIST AND SORT IT"""
def sort():
    mylist = []
    while(True):
        str = input("ENTER A STRING FOR THE LIST: ")
        mylist.append(str)
        ans = input("wanna add more?...")
        if(ans == "y" or ans == "Y"):
            continue
        else:
            break
    print(mylist)
    mylist.sort()
    print(mylist)