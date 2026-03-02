my_string = input("Enter Your String : ").lower()

unique_ch = []
for ch in my_string:
    if my_string.count(ch) > 1:
        continue
    else:
        unique_ch.append(ch)
        
print(unique_ch)
print(len(unique_ch))