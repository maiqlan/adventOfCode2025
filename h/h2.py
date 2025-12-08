import sys

# union find for merging efficiently
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.sze = [1]*n
        self.cost = [-1]*n
                
    def whichset(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.whichset(self.parent[x])
        return self.parent[x]

    def isSameSet(self, i, j):
        return self.whichset(i) == self.whichset(j)
    
    def merge(self, a, b):
        x = self.whichset(a)
        y = self.whichset(b)
        if x == y:
            return

        if self.sze[x]>self.sze[y]:
            self.parent[y]=x
            self.sze[x]+=self.sze[y]
            self.sze[y]=0
        else:
            self.parent[x] = y
            self.sze[y] += self.sze[x]
            self.sze[x]=0

    def returnSize(self, a):
        x = self.whichset(a)
        return self.sze[x]
    
    def setCost(self, a, cost):
        x = self.whichset(a)
        self.cost[x] = cost
        return

    def threelargestcircuits(self):
        sortedsze=self.sze
        sortedsze.sort(reverse=True)
        res=1
        for i in range(3):
            res*=sortedsze[i]
        
        return res

def euclid(a,b):
    x,y,z = a
    d,e,f = b
    o=(x-d)**2
    t=(y-e)**2
    p=(z-f)**2
    return (o+t+p)**(1/2)
    
junctions=[]

n = sys.stdin.readline().replace('\n','')
while n!="":
    junctions.append(tuple(map(int,n.split(','))))
    n = sys.stdin.readline().replace('\n','')


boxn=len(junctions)
UF = UnionFind(boxn)
EL=[]
for i,box1 in enumerate(junctions):
    for j,box2 in enumerate(junctions):
        if i>=j: #avoid connecting same node
            continue
        #create edges
        dist=euclid(box1,box2)
        EL.append((dist, i, j))
        
# we want to stop after we can say that all the values have been paired with something

paired_vals=set()
EL.sort()
con=0
for edge in EL:
    dist, i, j = edge
    UF.merge(i,j)
    if UF.returnSize(i)==boxn:
        x1,_,_ = junctions[i]
        x2,_,_ = junctions[j]
        print(x1*x2)
        break

print(UF.threelargestcircuits())

        