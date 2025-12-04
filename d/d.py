import sys

PART=1
dr = (1, 1, 0,-1,-1,-1, 0, 1)
dc = (0, 1, 1, 1, 0,-1,-1,-1)

#helper
def print2D(ary):
    for i in range(0, len(ary)):
        for j in range(0, len(ary[0])):
            print("{} ".format(ary[i][j]), end="")
        print("")
    print()

grid=[]
def procgrid():
    global grid
    a,b = len(grid),len(grid[0])
    def simple4check(i,j):
        global grid
        if grid[i][j] != '@':
            return 0
        
        loc=[]
        for k in range(8):
            loc.append((i+dr[k], j+dc[k]))
        
        papers=0
        for ni,nj in loc: #ni is y, nj is x, check 8 locations around
            if ni < 0 or nj < 0 or ni >= a or nj >= b: #oob
                continue
            elif grid[ni][nj]=='@':#valid num
                papers+=1
        
        if papers < 4:
            grid[i][j]='x'
            return 1
        return 0
    
    tot,val=0,0
    while True:   #this part was added for 
        for i in range(a):
            for j in range(b):
                val+=simple4check(i,j)
        print2D(grid)
        if val==0:
            break
        tot+=val
        val=0
        
        
    return tot
            
n = sys.stdin.readline().replace('\n','')
while n!="":
    grid.append([c for c in n])
    n = sys.stdin.readline().replace('\n','')
    
print2D(grid)
r=procgrid()
print(r)
