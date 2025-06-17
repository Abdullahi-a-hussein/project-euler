from problem3 import is_prime


def nth_prime(n: int) -> int:
    """
    return the nth <n> prime number
    """
    current = 3
    current_prime = 2
    i = 1
    while i < n:
        if is_prime(current):
            i += 1
            current_prime = current

        current += 2

    return current_prime


if __name__ == "__main__":
    n = 10_001
    print(nth_prime(n))
