my_tuple = (1,4,5,8,6,4,8,9,3,7)

even_tuple = ()
odd_tuple = ()

for num in my_tuple:
    if (num % 2 ==0):
        even_tuple = even_tuple +(num,)
    else:
        odd_tuple = odd_tuple + (num,)


print(odd_tuple)
print(even_tuple)