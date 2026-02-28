word = input("Enter Your Word : ").lower()

if word == word[::-1]:
    print(word ,"Is Palindrome")
else:
    print(word ,"Is not Palindrome")