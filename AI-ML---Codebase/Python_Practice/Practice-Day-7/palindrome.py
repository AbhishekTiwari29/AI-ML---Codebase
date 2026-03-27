# Write a program to check whether a number is a palindrome or not.

num = input("Enter Your Number: ")

if num == num[::-1]:
    print(f"{num} is Palindrome")
else:
    print(f"{num} is not Palindrome")

    