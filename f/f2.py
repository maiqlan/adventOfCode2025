import sys

def op(a:int,b:int,c):
    if c.strip()=='*':
        return a*b
    return a+b

n = sys.stdin.readline().replace('\n','')
val=[]
while n!="":
    val.append(n)
    n = sys.stdin.readline().replace('\n','')
    
operations = val.pop().split()
lv,lw,ls=len(val[0].split()),len(val),len(val[0])
result=0

def fetch(j):
    if j >=ls : return -1
    res = ""
    for i in range(lw):
        if val[i][j] != " ":
            res+= val[i][j]
    return int(res) if res != "" else -1

k=-1
for i in range(lv): #determines which operation to use
    k+=1
    if k >= ls:
        break
    
    value=fetch(k)
    # only break if we get all spaces
    while k < ls:
        k+=1
        evalv=fetch(k)
        if evalv == -1: 
            break #everything was a white space down so we gotta move onto next one 
        value = op(value, evalv, operations[i])
    result+=value

print(f"PART 2: {result}")
