import math


def solveTwoVar(a1, b1, c1, a2, b2, c2):
    return ((b2*c1 - b1*c2)/(a1*b2 - a2*b1), (a2*c1 - a1*c2)/(a2*b1 - a1*b2))


# (x, y) = solveTwoVar(1, 1, 36, 2, 4, 100)
# print(x, y)


def solve2Var(e):
    # solve x + y = e
    if e < 0:
        return []
    
    res = []

    for x in range(0,e):
        res.append((x, e - x))

    return res


def solve3Var(e):
    # solve x + y + z = e

    if e < 0:
        return []

    res = []

    for z in range(0, e):
        # solve x + y = e - z
        xy_list = solve2Var(e - z)
        for xy in xy_list:
            res.append((xy[0], xy[1], z))
    
    return res


# print(solve3Var(3))


def solve(a, b, c, d, e):
    """
    giai he phuong trinh nghiem nguyen duong
    x + y + z = e
    ax + by + cz = d
    """
    if (e < 0 or d < 0) or (a == b and a == c and d != e) or (a + b + c > d):
        return []
    elif a == b and a == c and d == e*a:
        return solve3Var(e)
    else:
        res = []
        
        for z in range(0, e):
            x = (d - b*e + (b - c)*z) // (a - b)
            # print(z, x)
            if (a - b)*x == d - b*e + (b - c)*z and x > 0:
                y = e - z - x
                # print(x, y, z)
                res.append((x, y, z))

        return res


print(solve(1, 2, 2, 11, 6))