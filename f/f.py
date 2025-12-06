import sys

def op(a:int,b:int,c):
    if c=='*':
        return a*b
    return a+b
       
n = sys.stdin.readline().replace('\n','')
val=[]
while n!="":
    inputval = list(n.split())
    val.append(inputval)
    n = sys.stdin.readline().replace('\n','')

operations = val.pop()
start=list(map(int,val.pop()))

for i in range(len(val)):
    args = map(int, val[i])
    for i, a in enumerate(args):
        start[i]=op(start[i], a, operations[i])

print(f"PART 1: {sum(start)}")
    