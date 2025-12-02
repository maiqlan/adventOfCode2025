import sys

def calc(r,s):
    a,b=s[0],int(s[1:])
    return (r-b) % 100 if a=="L" else (r+b) % 100

result,pwd=50,0
n = sys.stdin.readline().replace('\n','')
while n!="":
    result=calc(result,n)
    if result==0: 
        pwd+=1
    n=sys.stdin.readline().replace('\n','')
print(pwd)