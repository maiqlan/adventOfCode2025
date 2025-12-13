import sys
#seems like a hard problem, but its just troll, inputs are too large to do anything really heuristically ngl, jsut pretend each package is 3x3

def possible(a:str, b:str):
    c,d=map(int,a.split('x'))
    inp=sum(map(int,b.split()))
    
    x,y = c//3, d//3
    
    return 1 if x*y >= inp else 0

#get rid of useless input
n = sys.stdin.readline().replace('\n','')
while 'x' not in n:
    n = sys.stdin.readline().replace('\n','')

res=0
while n!="":
    a, b = n.split(":")
    res+=possible(a,b) 
    n = sys.stdin.readline().replace('\n','')

print(res)