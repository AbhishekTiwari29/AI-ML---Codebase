string = input("ENTER A STRING: ")

count = 0

for ch in string:
    if ch == " ":
        count +=1

print("TOTAL NO> OF SPACES : ",count)