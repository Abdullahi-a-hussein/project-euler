from math import floor, sqrt


def highly_divisible_numbers(terminate):
    i = 7
    target = triangle_number(i)
    counter = factors(target)
    while counter <= terminate:
        i += 1
        target = triangle_number(i)
        counter = factors(target)
    return target


def factors(n: int) -> list[int]:
    """
    Return all the divisors of <n>
    """

    factor = [1]
    # TODO: find all factors of n
    r = floor(sqrt(n))
    for i in range(2, r + 1):
        if n % i == 0:
            factor.append(i)
            if r * r != n:
                factor.append(n // i)
    return len(factor) + 1


def triangle_number(n: int) -> int:
    """
    Return the <n>th triangle number
    """
    return sum([i for i in range(1, n + 1)])


if __name__ == "__main__":
    # test example
    terminate = 5
    print(highly_divisible_numbers(5))
    terminate = 500
    print(highly_divisible_numbers(terminate))
