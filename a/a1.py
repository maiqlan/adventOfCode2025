import sys
import re

n = sys.stdin.readline().replace('\n','')
pattern = r"(L|R)(\d+)"

def calc(r,s):
    match = re.findall(pattern, s)
    for a,b in match:
        if a == "L":
            r=(r-int(b)) % 100
        else:
            r=(r+int(b)) % 100
    return r

result=50
pwd=0
while n!="":
    result=calc(result,n)
    if result==0: 
        pwd+=1

    n=sys.stdin.readline().replace('\n','')
print(pwd)

