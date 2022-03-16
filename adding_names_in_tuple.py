"""adding names in tuple"""
t1 = ()
t2 = ()
r = int(input("Enter the range: "))
for i in range(r):
    n = input("Enter the names: ")
    t1 = (n,)
    t2 = t2 + t1
print(t2)