list1 = [1,2,3,4]
list2 = [5,6,3,7,8]

if set(list1).isdisjoint(set(list2)):
    print("NO COMMON ELEMENT")
else:
    print("COMMON ELEMENT")