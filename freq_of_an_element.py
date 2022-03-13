def cnt():
    l = [1,2,3,2,4,1,5,6,9,1,5,1]
    ele = 1
    count = 0
    for i in range(len(l)):
        if ele == l[i]:
            count +=1
    print(l)
    print(ele,"has frequency",count)