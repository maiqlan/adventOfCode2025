import sys
from collections import defaultdict

EL,VIS,V=defaultdict(list),defaultdict(bool),defaultdict(int)
topo=[]

def paths(s):
    global topo,V
    
    def dfs(v):
        global V
        VIS[v]=True;
        for u in EL[v]:
            if VIS[u]: continue
            dfs(u)
        topo.append(v)
   
    dfs(s)         
    topo.reverse()
    
    # using ans, we will calc svr -> a -> b -> out (with a and b being whatever respective value lol), traverse in topological order
    V[s]=1
    fft,dac=-1,-1
    for v in topo:
        if v=="fft":
            fft=V[v]
            V=defaultdict(int)
            V[v]=1
        elif v=="dac":
            dac=V[v]
            V=defaultdict(int)
            V[v]=1 # reset
            
        for e in EL[v]:
            V[e]+=V[v] # calculate all the ways to get to this value

    print(fft*dac*V["out"])    
    

n = sys.stdin.readline().replace('\n','')
while n!="":
    a, b = n.split(":")
    EL[a]=b.split()
    n = sys.stdin.readline().replace('\n','')

paths("svr")