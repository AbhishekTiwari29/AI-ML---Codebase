def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Example test
print(is_prime(7))   # True
print(is_prime(9))   # False
print(is_prime(2))   # True
print(is_prime(1))   # False