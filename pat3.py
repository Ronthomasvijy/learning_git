def diamond(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + 'o' * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + 'o' * (2 * i - 1))

diamond(5)