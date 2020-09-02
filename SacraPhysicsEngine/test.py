from random import randint
from SacraMathEngine import *
import sys
sys.setrecursionlimit(2000)

XYPlane = []
for i in range(10):
    ZPlane = []
    for k in range(10):
        ZPlane.append(vec3d(i,0,k))
    XYPlane.append(ZPlane)
#print(XYPlane)

def PerlinBuilder(Mesh):
    for i in range(1, len(Mesh)):
        for k in range(1, len(Mesh[i])):
            Value = randint(Mesh[i-1][k].y - 2, Mesh[i][k-1].y + 2)
            Mesh[i][k].y = Value
PerlinBuilder(XYPlane)
print(XYPlane)
