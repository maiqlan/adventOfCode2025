import sys
sys.setrecursionlimit(10**6)
import heapq

#certainly not efficient, will redo at a later date, nlogn operations are not ideal :(
PART=2

# extremely scuffed solution fmsbcl, other solution could be applied here as well but with search space different
def determineMax1(n):
    ni = [(int(c), i) for i, c in enumerate(n)]
    ni.sort(key=lambda x: (-x[0], x[1]))
    start, ind = ni[0]
    
    nr = [(int(c), i) for i, c in enumerate(n[:ind])]
    nl = [(int(c), i) for i, c in enumerate(n[ind+1:])]

    nr.sort(key=lambda x: (-x[0], x[1]))
    nl.sort(key=lambda x: (-x[0], x[1]))
   
    r= nr[0][0] if len(nr) > 0 else 0
    l= nl[0][0] if len(nl) > 0 else 0
 
    if l!=0 and r!=0:
        return max(r*10+start,start*10+l)
    elif l==0:
        return r*10+start
    else:
        return start*10+l
    

def determineMax2(n):
   #get the top 12 ideal maximizing numbers, this rises from the observation that the first possible digit of the sequence lies within a range in n, the second, and so on
    n=list(map(int,n))
    stack,ans=[],[]
    recent,a=0,0
    heapq.heapify(stack)
    
    for i in range(len(n)-12): #the first digit must be in range len(n)-12-0
        heapq.heappush(stack,(-n[i],i))

    for i in range(12):
        heapq.heappush(stack,(-n[len(n)-12+i],len(n)-12+i) )
        while stack[0][1] < recent: #remove values that preceed the recent index because no longer valid
            heapq.heappop(stack)
        
        c, recent = heapq.heappop(stack)
        ans.append(-c)
        a+= ans[-1] * pow(10, 12-i-1)
    return a
    
   
r=0
n = sys.stdin.readline().replace('\n','')
while n != "":
    if PART==1:
        r+= determineMax1(n)
    else:
        r+= determineMax2(n)
    n = sys.stdin.readline().replace('\n','')

print(r)