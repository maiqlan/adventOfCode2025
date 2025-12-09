import sys
from shapely.geometry import LineString
from shapely.geometry.polygon import Polygon
from shapely import prepare

polygon=None
def dist(a,b):
    x1,y1=a
    x2,y2=b
    dx=x1-x2
    dy=y1-y2

    if x1==x2 and y1!=y2 or x1!=x2 and y1==y2 and polygon.contains(LineString([a,b])):
        return (abs(dx)+1) * (abs(dy)+1)

    if polygon.contains(Polygon([a, (x1, y2), b, (x2, y1)])):
        return (abs(dx)+1) * (abs(dy)+1)
    return 0

inp=[]
n = sys.stdin.readline().replace('\n','')
while n!="":
    inp.append(tuple(map(int,n.split(','))))
    n = sys.stdin.readline().replace('\n','')

prepare(Polygon(inp))
maxdist=-1
for i in range(len(inp)):
    for j in range(len(inp)):
        if i>=j: 
            continue
        d=dist(inp[i],inp[j])
        maxdist=max(maxdist, d)

print(maxdist)