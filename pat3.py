def diamond(n):
    l=0
    for i in range(1, n + 1):
        print(' ' * (n - i) + chr(ord('A')+l) * (2 * i - 1))
        l+=1
    l-=1
    for i in range(n - 1, 0, -1):
        l-=1
        print(' ' * (n - i) + chr(ord('A')+l) * (2 * i - 1))
diamond(5)