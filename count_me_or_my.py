with open("STORY.TXT","r") as spcin:
    n=0
    a=spcin.read()
    words=a.split()
    for i in words:
        if i=="me" or i=="Me" or i=="my" or i=="My":
            n+=1
    print("Count of Me/My in the file: ",n)

spcin.close()