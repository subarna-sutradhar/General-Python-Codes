#writing lines in a single line with line break
def writelines():
    f = open(r'F:\python 3.8 progs\readandwrite02.txt','w+')

    while(True):
        l = input("ENTER A LINE: ")
        a = l + "\n"
        f.write(a)
        ans = input("WANNA CONTINUE?Y/N: ")
        if(ans == "N" or ans == "n"):
            break

    f.seek(0)
    print(f.readlines())