def even_fibonacci(n):
    """
    find the sum of the even-valued terms less than or equal to n.
    """
    total = 0
    j, i = 1, 2
    while i <= n:
        if i % 2 == 0:
            total += i
        j, i = i, i + j
    return total


print(even_fibonacci(4_000_000))
