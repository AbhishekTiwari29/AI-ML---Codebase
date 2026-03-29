# Write a program to remove duplicate characters from a string.

text = "AbhishekTiwari "

result = ""

for ch in text:
    if ch not in result:
        result += ch
    
print(result)