import sys 

ingredients,ranges,res=[],[],[]

# BINARY SEARCH FOR THE SOLUTION
def binsearch(ingredient):
    lo,hi=0,len(res)-1

    while(lo <= hi):
        mid = (lo+hi)//2
        a,b = res[mid]
        
        if a <= ingredient and b >= ingredient:
            return 1
        
        if ingredient<a: # if a is less than ing val, we want to search the lower side    
            hi=mid-1 
        else:
            lo=mid+1
                
    return 0 #exhaust search

def mergeOverlap(arr):
    arr.sort()
    res.append(arr[0])

    for i in range(1, len(arr)):
        curr = arr[i]

        if curr[0] <= res[-1][1]: #if overlapping (e.g. the start range for the thing to be appended is less than or equal to the end range of the previous)
            res[-1][1] = max(res[-1][1], curr[1])  #merge
        else:
            res.append(curr)
    return res


n = sys.stdin.readline().replace('\n','')
while n!="":
    a,b = map(int,n.split('-'))
    ranges.append([a,b])
    n = sys.stdin.readline().replace('\n','')
    
res = mergeOverlap(ranges)
fresh=0
for a, b in res:
    fresh+= b-a+1

fresh2=0
n = sys.stdin.readline().replace('\n','')
while n!="":
    fresh2+=binsearch(int(n))
    n = sys.stdin.readline().replace('\n','')

print(f"PART 1 ANSWER: {fresh2}")
print(f"PART 2 ANSWER: {fresh}")