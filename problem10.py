from math import floor, sqrt


def primes(n):
    """
    returns the sum of all primes less than <n>
    """
    summed = 2 + 3 + 5 + 7

    f = 11
    while f < n:
        prime1 = is_prime(f)
        prime2 = is_prime(f + 2)
        if prime1:
            summed += f
        if prime2:
            summed += (f + 2)
        f += 6
    return summed


def is_prime(n: int) -> bool:
    """
    Return True if n is prime. False otherwise
    """
    # every prime  equal to or greater than 5 can be written as 6k -/+ 1

    if n == 1:
        return False
    if n < 4:
        return True

    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    r = floor(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


if __name__ == "__main__":
    n = 2_000_000
    print(primes(n))
