def calCos(x, n):
    sum = 1
    mem = 1
    for i in range(0,n):
        mem = - mem * (x**2) / ((2*i + 1) * (2*i + 2))
        # print(f'mem: {mem}')
        sum = sum + mem
    return sum

cos = calCos(0.94, 10)
print(cos)

def abs(x):
    return x if x >= 0 else -x

def calCosTol(x, e):
    sum = 1
    mem = 1
    i = 0
    while abs(mem) > e:
        mem = - mem * (x**2) / ((2*i + 1) * (2*i + 2))
        # print(f'mem: {mem}')
        sum = sum + mem
        i = i + 1
    return sum 
       
cosTol = calCosTol(1.2, 0.02)
print(cosTol)

