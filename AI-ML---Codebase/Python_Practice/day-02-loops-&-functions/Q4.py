def count_digit(n):
    count = 0

    while n>0:
        n = n//10
        count += 1

    return count

print(count_digit(13254968))