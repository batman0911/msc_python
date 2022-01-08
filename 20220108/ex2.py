import math

a = float((input()))
b = float((input()))
c = float((input()))

def isTriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(f'is triangle: {isTriangle(a,b,c)}')

if(isTriangle(a, b, c)):
    p = a + b + c
    print(f'chu vi tam giac: {p}')
    print(f'dien tich tam giac: {math.sqrt(p*(p-a)*(p-b)*(p-c))}')