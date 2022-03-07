"""Interchanging tuples"""
def tup():
    t1 = (1,2,3)
    print("Original t1: ",t1)
    t2 = (4,5,6)
    print("Original t2: ",t2)
    t2,t1 = t1,t2
    print("AFTER INTERCHANGING")
    print("t1: ",t1)
    print("t2: ",t2)
