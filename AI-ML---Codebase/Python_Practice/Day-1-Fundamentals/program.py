#  1  #

name = input("Enter your Name : ")
age = input("Enter your Age : ")

print("Hello "+ name +", you are "+ age +" years old" )


#  2  #

a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)


#   3   #

first = int(input("Enter First Number"))
second = int(input("Enter Second Number"))
third = float(input("Enter Third Number"))

average = float((first+second+third)/3)

print(average)



#  4  #

string = str(input("enter a number"))

string_int = int(string)
string_float = float(string_int)
string_again_str = str(string)


print(string_int)
print(type (string_int))
print(string_float)
print(type (string_float))
print(string_again_str)
print(type (string_again_str))


#  5  #

x = 10 + 3 * 2 ** 2 
print(x)



#  6  #



a = int(input("Enter first number : " ))
b = int(input("Enter second number : " ))

temp = a
a = b
b = temp

print("First Number : ", a)
print("Second Number : ", b)



#  7   #


Temp_cel = input("Enter Temperature : ")

Temp_in_float  =  float(Temp_cel)

Temp_fert = (Temp_in_float*(9/5))+32

print("your temperature is : ", Temp_fert )


#   8   #


r = int(input("Enter Radius : "))

area = float(3.14 * r*r)

print("Area : ",area)



#    9    #


p = int(input("Enter Principle"))
r = int(input("Enter Rate"))
t = int(input("Enter Time"))


si = float((p* r *t)/100)

print("SI is : ",si)


#    10    #



num = input("Enter your number")

num_float = float(num)

integer_part = int(num_float)
decimal_part = int((num_float - integer_part)*100)


print("Integer Part : ", integer_part)
print("Decimal Part : ", decimal_part)

