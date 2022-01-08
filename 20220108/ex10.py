import math

def solveTwoVar(a1, b1, c1, a2, b2, c2):
    return ((b2*c1 - b1*c2)/(a1*b2 - a2*b1), (a2*c1 - a1*c2)/(a2*b1 - a1*b2))

(x, y) = solveTwoVar(1, 1, 36, 2, 4, 100)
print(x, y)

