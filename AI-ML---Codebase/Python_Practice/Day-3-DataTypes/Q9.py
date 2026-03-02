my_list = [1,3,5,8,6,4,1,1,2,4,5,6,8,9,7,4,5,3,12,48,557,45,48]

result= []

for num in my_list:
    if my_list.count(num) > 1 and num not in result:
        result.append(num)

print(result)