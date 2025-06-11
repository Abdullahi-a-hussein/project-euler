def largest_palindrome_product(digits):
    """
    Return the largest palindrome number that is made of the product 
    of two three-digit numbers"
    """
    digit1 = (10 ** (digits - 1) + 1)
    current_palindrome = 0
    while digit1 < 10 ** digits:
        digit2 = (10 ** (digits - 1) + 1)
        while digit2 < 10 ** digits:
            product = digit1 * digit2
            if product > current_palindrome and is_palindrome(product):
                current_palindrome = product
            digit2 += 1
        digit1 += 1
    return current_palindrome


def is_palindrome(number):
    current = str(number)
    reverse = ""
    i = len(current) - 1
    while i >= 0:
        reverse += current[i]
        i -= 1
    return current == reverse


print(largest_palindrome_product(3))
