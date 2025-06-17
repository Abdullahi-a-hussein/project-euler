def sum_of_squares(n):
    squared_sum = sum([i**2 for i in range(1, n + 1)])
    sum_squared = (sum([i for i in range(1, n + 1)]))**2
    return sum_squared - squared_sum


if __name__ == "__main__":
    n = 100
    print(sum_of_squares(n))
