def multiple3_or_5(n):
    """
    Return the sum of all numbers less than <n> that is either muliple of 
    5 or 3
    """
    total = 0
    for i in range(2, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


print(multiple3_or_5(1000))
