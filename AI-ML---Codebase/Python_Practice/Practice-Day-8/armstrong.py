# Write a program to check whether a number is an Armstrong number or not.


num = int(input("enter your number: "))
total = 0
digits = len(str(num))
for n in str(num):
    n= int(n)
    n = n**digits
    total +=n

if total == num:
    print(f"{num} is Armstrong Number")
else:
    print(f"{num} is Not a Armstrong Number")