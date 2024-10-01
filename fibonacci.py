def fibonacci(n: int):
    if n < 2:
        return n
    else:
        x, y = 0, 1
        # here we are memoized and not using recursion for algorithm optimization
        for _ in range(2, n + 1):
            x, y = y, x + y
        return y


if __name__ == "__main__":
    print(fibonacci(7))
