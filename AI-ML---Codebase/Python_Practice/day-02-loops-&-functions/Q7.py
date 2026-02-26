while True:
    n = input("ENTER YOUR NUMBER : ")
    if (n == "quit"):
        break
    n =int(n)

    if (n >0):
        print("POSITIVE NUMBER")
    elif(n<0):
        print("NEGATIVE NUMBER")
    