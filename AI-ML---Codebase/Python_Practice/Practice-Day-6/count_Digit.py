# Write a program to count how many digits are in a given number.

num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10   # last digit remove
    count += 1

print("Total digits:", count)