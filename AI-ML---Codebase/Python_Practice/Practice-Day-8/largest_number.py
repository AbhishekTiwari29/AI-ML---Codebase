# Write a program to find the largest number in a given list.

numbers = [1,2,5,4,8,9,6,4,5,11]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"largest number is {largest}")