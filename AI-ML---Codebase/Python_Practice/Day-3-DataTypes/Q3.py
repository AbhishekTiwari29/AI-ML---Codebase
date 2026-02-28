list1 = [1,3,5,8,64,45]
list2 = [1,3,5,9,45,55]

list1 = set(list1)
list2 = set(list2)

new_list = list1.union(list2)
new_list = list(new_list)

new_list.sort()
print(new_list)


