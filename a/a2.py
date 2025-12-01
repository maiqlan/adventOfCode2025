import sys
import re

n = sys.stdin.readline().replace('\n','')
pattern = r"(L|R)(\d+)"

def calc(r,s):
    match = re.findall(pattern, s)
    t=-1
    for a,b in match:
        if a == "L":
            t=(r-int(b)) % 100
        else:
            t=(r+int(b)) % 100
    
    if match[0][0]=="L" and r<=int(b) and r==0: #will be negative
        return t, (int(b)-r) // 100
    elif match[0][0]=="L" and r<=int(b):
        return t, (int(b)-r) // 100 + 1
    elif match[0][0]=="R" and (r+int(b))>=100:
        return t, (r+int(b))//100
        
    return t,1 if t==0 else 0

result=50
pwd=0
while n!="":
    r,p=calc(result,n)
    pwd+=p
    result=r
    print(r,p)
    n=sys.stdin.readline().replace('\n','')
print(pwd)

