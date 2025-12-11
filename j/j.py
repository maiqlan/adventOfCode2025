import sys, copy
from collections import defaultdict
# figure out least amount of buttons to xor to get the result
# one way we can do this is by converting a to bit format, and then for each elemetn in the basis, keep trying to reduce b
def calcFewest(v):
    a, *b, _ = v
    l = len(a)-2

    def buttontobit(b:str):
        res=0
        bc=map(int,b.strip("()").split(","))
        for p in bc:
            res |= 1 << (l-p-1)
        return res

    def indicatortobit(b:str):
        res=0
        for i in range(len(b)):
            if b[i]=='#':
                res |= 1 << (l-i-1)
        return res

    def bruteforcebit(a,b:list):
        b.sort(reverse=True)
        for item in b:
            if a==item:
                return 1
        totcombos=defaultdict(set)
        totcombos[1]=set(copy.deepcopy(b))
        for i in range(1, len(b)):
            for item in totcombos[i]: #multiply every item in the previous set 
                for lb in b:
                    cand=item^lb
                    if cand==a:
                        return i+1 #took i+1 steps to get the result
                    if cand not in totcombos[i]: #ensure that this xor doesnt undo stuff, if it does, then was a useless operation
                        totcombos[i+1].add(cand)
        return 0
    abit=indicatortobit(a[1:-1])
    bbit=list(map(buttontobit, b)) 
    return bruteforcebit(abit, bbit)
    
res=0
n = sys.stdin.readline().replace('\n','')
while n!="":
    res+=calcFewest(n.split(" "))
    n = sys.stdin.readline().replace('\n','')

print(res)
