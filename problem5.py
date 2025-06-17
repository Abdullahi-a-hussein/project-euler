def smallest_multiple(numbers: list) -> int:
    """
    Return the smalest multiple of the numbers in the list numbers
    """
    if len(numbers) == 2:
        return lcm(numbers[0], numbers[1])
    computed = lcm(smallest_multiple(numbers[:-1]), numbers[-1])
    return computed


def gcd(number1: int, number2: int) -> int:
    """
    Return the greatest common divider of numbers <number1> and <number2>.
    """
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def lcm(number1: int, number2: int) -> int:
    """
    Return the lcm of numbers <number1> and <number2>
    lcm(a, b) = |a x b|/gcd(a, b)
    """
    return (number1 * number2) // gcd(number1, number2)


if __name__ == "__main__":
    numbers = [i for i in range(1, 21)]
    print(smallest_multiple(numbers))
