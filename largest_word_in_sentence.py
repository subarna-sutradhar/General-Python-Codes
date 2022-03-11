"""add a sentence and show the largest word in it"""
def large():
    largwrd = None
    maxlen = 0
    st = input("enter a sentence: ")
    word = st.split()
    print(word)
    for i in word:
        if(len(i)>maxlen):
            maxlen = len(i)
            largwrd = i
    print("the largest word is {} of length {}".format(largwrd,maxlen))