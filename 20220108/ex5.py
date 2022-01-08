def doubleFac(n):
    res = 1
    i = 1

    if n % 2 == 0:
        i = 2
    else:
        i = 3

    while i <= n:
        res = res * i
        i = i + 2
    return res

print(doubleFac(6))