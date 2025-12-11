import sys
from scipy.optimize import linprog

def calcFewest(v):
    _, *b, c = v
    def buttontoint(b:str):
        return tuple(map(int,b.strip("()").split(",")))

    def counter(b:list,c:list):
        #linear programming
        A_eq=[[0]*len(b) for _ in c]
        for i,tup in enumerate(b):
            for t in tup:
                A_eq[t][i]=1
        res = linprog([1]*len(b), A_eq=A_eq, b_eq=[c], integrality=[1]*len(b))
        
        return int(sum(res.x)) # eh idk
    
    return counter(list(map(buttontoint, b)),list(map(int,c[1:-1].split(','))))
    
res=0
n = sys.stdin.readline().replace('\n','')
while n!="":
    res+=calcFewest(n.split(" "))
    n = sys.stdin.readline().replace('\n','')
print(res)
