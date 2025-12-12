import sys
from collections import defaultdict, deque

EL=defaultdict(list)
V=defaultdict(int) #visited/how many ways we can get to this value
def paths(s):
    bfs = deque()
    bfs.append(s)
    
    while len(bfs) != 0:
        u = bfs.popleft()
        V[u]+=1

        for v in EL[u]:
            bfs.append(v)    
    

n = sys.stdin.readline().replace('\n','')
while n!="":
    a, b = n.split(":")
    EL[a]=b.split()
    n = sys.stdin.readline().replace('\n','')


paths("you")
print(V["out"])