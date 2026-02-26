salary = int(input("Enter Your Salary : "))

if (salary <= 30000):
    print("Tax is : ", (5/100)*salary)
elif (salary > 30000 and salary <= 70000):
    print("Tax is : " ,(15/100)*salary)
else:
    print("tax is : ", (20/100)*salary)