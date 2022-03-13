#writing lines in a single line without line break
def writelines():
    f = open(r'F:\python 3.8 progs\readandwrite01.txt','w+')

    while(True):
        l = input("ENTER A LINE: ")
        f.write(l)
        ans = input("WANNA CONTINUE?Y/N: ")
        if(ans == "N" or ans == "n"):
            break

    f.seek(0)
    print(f.readlines())