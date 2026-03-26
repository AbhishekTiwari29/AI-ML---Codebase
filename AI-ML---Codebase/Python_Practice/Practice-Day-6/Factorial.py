# Write a program to find the factorial of a given number.

def factorial(n):
    total = 1
    for i in range(1,n+1):
        total = total * i
    print(f"Factorial of {n} is {total}")

factorial(5)
