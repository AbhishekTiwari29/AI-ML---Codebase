def sum_digit(n):
    sum = 0

    for digit in str(n):
        sum += int(digit)
    print(sum)

sum_digit(3214156)