import sys

PART=2

#lazy brute force, could probably solve this with a calculation ngl
def findInvalidID(a,b):
    l,r,val=len(a),len(b),0 #string manipulation is the goat here
    for i in range(l,r+1):
        if i % 2==1:
            continue
        start = pow(10, i//2 - 1)
        for j in range(start, start*10):
            cand=int(str(j)*2)
            if cand < int(a):
                continue
            if cand <= int(b):
                val+=cand
            elif cand > int(b):
                break 
    return val

def findInvalidID2(a,b):
    l,r,val=len(a),len(b),0 #string manipulation is the goat here
    validnums=set()
    for i in range(l,r+1): # i is the length of possible string, this is to get within range a-b
        for k in range(1, i//2 + 1): # length of the repeat string , so like {1}{1}{1}{1} vs {10}{10}
            if i//k < 2 or i//k *k != i: continue
            start = pow(10, k-1)
            for j in range(start, min(start*10, int(b))):
                cand=int(str(j)*(i//k))
                if cand < int(a):
                    continue
                if cand <= int(b):
                    if cand not in validnums:
                        validnums.add(cand)
                        val+=cand
                elif cand > int(b):
                    break 
    return val
n = sys.stdin.readline().replace('\n','').split(',')

invalid=0
for i in n:
    a,b = i.split('-')
    if PART==1:
        invalid+=findInvalidID(a,b)
    else:
        invalid+=findInvalidID2(a,b)

print(f"invalid = {invalid}")