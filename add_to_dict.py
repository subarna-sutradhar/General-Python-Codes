def addtodict():
    rr = dict()
    n = int(input("HOW MANY ELEMENTS? "))
    for i in range(n):
        ka = int(input("ADD KEY: "))
        kv = int(input("ADD VALUE: "))
        rr[ka] = kv
    print(rr)