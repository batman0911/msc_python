import util

def printPerfectSquare(n):
    for i in range(0,n):
        if util.isPerfectSquare(i):
            print(i)

printPerfectSquare(10)