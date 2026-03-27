# Write a program to count how many vowels (a, e, i, o, u) are present in a string.

str = input("Enter Your String: ")
count = 0
for ch in str:
    if ch.lower() == "a" or ch == "e" or ch =="i" or ch =="o" or ch =="u":
        count += 1

print(count)

