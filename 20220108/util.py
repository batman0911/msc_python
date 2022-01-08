import math

def isPerfectSquare(n):
    s = int(math.sqrt(n))
    return s**2 == n

def isIntTuple(t):
    for e in t:
        if not isinstance(e, int):
            return False
    return True

# t = (1, 2, 4, 2.0)
# print(isIntTuple(t))

def solveTwoVar(a1, b1, c1, a2, b2, c2):
    return ((b2*c1 - b1*c2)/(a1*b2 - a2*b1), (a2*c1 - a1*c2)/(a2*b1 - a1*b2))

# (x, y) = solveTwoVar(1, 1, 36, 2, 4, 100)
# print(x, y)

def perfectSquareInRage(n):
    res = []
    for i in range(1, n):
        if isPerfectSquare(i):
            res.append(i)
    return res

# p = perfectSquareInRage(10)
# print(p)