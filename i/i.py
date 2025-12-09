import sys

def dist(a,b):
    x1,y1=a
    x2,y2=b
    dx=x1-x2
    dy=y1-y2
    return (abs(dx)+1) * (abs(dy)+1)

inp=[]
n = sys.stdin.readline().replace('\n','')
while n!="":
    inp.append(tuple(map(int,n.split(','))))
    n = sys.stdin.readline().replace('\n','')

inp.sort()

maxdist=-1
for i in range(len(inp)):
    for j in range(len(inp)):
        if i>=j: 
            continue
        d=dist(inp[i],inp[j])
        maxdist=max(maxdist, d)

print(maxdist)