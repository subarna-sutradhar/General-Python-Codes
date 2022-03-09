"""linear search"""
def sear():
    l = [2,6,9,7,5,1]
    s = 7
    min_index = 0
    for i in range(len(l)-1):
        if s == l[i]:
            min_index = i
    print(s,"found at  ",min_index)
    