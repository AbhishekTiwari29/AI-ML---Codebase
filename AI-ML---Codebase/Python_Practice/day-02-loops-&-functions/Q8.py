def calculator(a,b,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator =="/":
        if b == 0:
            return "cannot divided by Zero"
        return a/b
    else:
        return "invalid operator"


result = calculator(5,6,"/")
print(result)