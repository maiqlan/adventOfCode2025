import sys

def print2D(ary):
    for i in range(0, len(ary)):
        for j in range(0, len(ary[0])):
            print("{} ".format(ary[i][j]), end="")
        print("")
    print()
    
tree,memo=[],[]
#UNIQUE PATHS PROBLEM
def dp(i,j):
    global tree, memo

    for i in range(1,len(tree)):
        for j in range(len(tree[0])):
            #calculate how many possible ways to reach [i][j] based on prior stuff
            if tree[i][j]=='^':
                memo[i][j] == 0
            elif tree[i][j]=='.':
                # three ways we can reach this square
                if j+1 < len(tree[0]) and tree[i][j+1]=='^':
                    #add all the numbers from above the carat
                    memo[i][j]+=memo[i-1][j+1]
                if j-1 < len(tree[0]) and tree[i][j-1]=='^':
                    #add all the numbers from above the carat       
                    memo[i][j]+=memo[i-1][j-1]
                #by default inherit stream from above
                memo[i][j] += memo[i-1][j]
                    
    
n = sys.stdin.readline().replace('\n','')
while n!="":
    tree.append([c for c in n])
    n = sys.stdin.readline().replace('\n','')

Spos=-1
for i in range(len(tree[0])):
    if tree[0][i] == 'S':
        Spos=i
        break

memo = [[0]*len(tree[0]) for _ in range(len(tree))]
memo[0][Spos]=1 #only one way to get to this position

dp(1, Spos)
print(sum(memo[-1]))