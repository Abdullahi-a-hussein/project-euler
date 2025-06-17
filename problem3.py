from math import sqrt


def largest_prime_factor(n):
    """
    Return the largest prime factor of <n>
    """
    current = n
    current_prime = 2
    i = 2
    while i < current:
        if is_prime(current):
            return current
        if current % i == 0 and is_prime(i):
            current_prime = i
            current = current // i
        i += 1
    return current_prime


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(sqrt(n))
    i = 3
    while i <= sqrt_n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
