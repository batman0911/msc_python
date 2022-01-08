import math

a = float((input()))
b = float((input()))
c = float((input()))

global x

def solve(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                raise Exception('phuong trinh co vo so nghiem')
            else:
                raise Exception('phuong trinh vo nghiem')
        else:
            return c / b
    
    delta = b*b - 4*a*c
    if(delta < 0):
        raise Exception('phuong trinh vo nghiem')
    elif delta == 0:
        return b / (2*a)
    else:
        return ((b + math.sqrt(delta)) / (2*a), (b - math.sqrt(delta)) / (2*a))

x = solve(a, b, c)
print(x)





        