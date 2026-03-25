# Write a program to calculate the sum of first n natural numbers.

n = int(input("Enter Your Number: "))
sum = 0

for i in range(1,n+1):
    sum = sum + i

print(sum)
