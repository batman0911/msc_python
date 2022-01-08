import util

def pythagoreSet(n):
    pfsq_list = util.perfectSquareInRage(n)
    res = []

    print(pfsq_list)
    
    for i in range(0, len(pfsq_list)):
        # print(pfsq_list[i])
        a = pfsq_list[i]
        for j in range(i, len(pfsq_list)):
            b = a + pfsq_list[j]
            if b in pfsq_list[j:len(pfsq_list)]:
                res.append((a, pfsq_list[j], b))
    
    return res

print(pythagoreSet(200))