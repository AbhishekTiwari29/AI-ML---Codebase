# Write a program to print the first n terms of Fibonacci series

n = int(input("enter your number: "))

a = 0
b = 1
c = 0

while c <=n:
    print(c)
    a = b
    b = c
    c = a+b

