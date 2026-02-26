a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

if a>b:
    a,b = b,a

a+=1

if a%2 != 0:
    a+=1

for i in range(a,b,2):
    print(i)