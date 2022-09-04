
umm = []


def selfNum(n):
    while n <= 10000:
        if n >= 1000 and n <= 9999:
            f = n + (n // 1000) + ((n // 100) %
                                   10) + ((n // 10) % 10) + (n % 10)
        elif n >= 100 and n <= 999:
            f = n + (n // 100) + ((n // 10) % 10) + (n % 10)
        elif n >= 10 and n <= 99:
            f = n + (n // 10) + (n % 10)
        else:
            f = n + n
        umm.append(f)
        n += 1
    for a in range(1, 10000):
        if a not in umm:
            print(a)


selfNum(1)
