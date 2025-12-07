import sys

def print2D(ary):
    for i in range(0, len(ary)):
        for j in range(0, len(ary[0])):
            print("{} ".format(ary[i][j]), end="")
        print("")
    print()
    
tree=[]

def proceed(i,j):
    global tree
    if i < 0 or j < 0 or i >= len(tree) or j >= len(tree[0]):
        return 0 # out of range, no split occurs
    
    if tree[i][j]=='.':
        tree[i][j]='|'
        return proceed(i+1, j)
    if tree[i][j]=='^':
        if j+1 < len(tree[0]):
            tree[i][j+1]='|'
        if j-1 >=0:
            tree[i][j-1]='|'
        return proceed(i+1, j+1) + proceed(i+1, j-1) + 2
    
    return 0
    
n = sys.stdin.readline().replace('\n','')
while n!="":
    tree.append([c for c in n])
    n = sys.stdin.readline().replace('\n','')

Spos=-1
for i in range(len(tree[0])):
    if tree[0][i] == 'S':
        Spos=i
        break

print(proceed(1, Spos))
print2D(tree)
