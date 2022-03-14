l1 = [1,2,3,4]
l2 = [5,6,1,7]
print(l1)
print(l2)
for i in range(len(l1)):
    ele = l1[i]
    if ele in l2:
        print("overlaped")
        break
else:
    print("separated")