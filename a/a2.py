import sys

def calc(r,s):
    a,b,t=s[0],int(s[1:]),-1
    t=(r-b) % 100 if a=="L" else (r+b) % 100
    
    if a=="L" and r<=b and r==0: #will be negative
        return t, (b-r) // 100
    elif a=="L" and r<=b:
        return t, (b-r) // 100 + 1
    elif a=="R" and (r+b)>=100:
        return t, (r+b)//100
        
    return t,1 if t==0 else 0

result,pwd=50,0
n = sys.stdin.readline().replace('\n','')
while n!="":
    result,p=calc(result,n)
    pwd+=p
    n=sys.stdin.readline().replace('\n','')
print(pwd)

