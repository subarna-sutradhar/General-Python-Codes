#Displaying names without vowels
def vow():
    while (True):
        str = input("Enter a string: ")
        for i in str:
            if i not in "aeiouAEIOU":
                print(i,end = "")
            print("")
            ans = input("Continue? ")
            if ans == "n" or ans == "N":
                break
vow()