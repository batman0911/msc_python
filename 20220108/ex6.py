def calSin(x, n):
    sum = x
    mem = x
    for i in range(0,n):
        mem = - mem * (x**2) / ((2*i +2) * (2*i + 3))
        print(f'mem: {mem}')
        sum = sum + mem
    return sum

sin = calSin(0.94, 10)
print(sin)