from random import randint
from SacraMathEngine import *

def Helper(ListOfVectors):
    for i in range(len(ListOfVectors)):
        Counter = True
        def Helper2():
            Value = randint(ListOfVectors[i-1].y -5, ListOfVectors[i-1].y +5)
            return Value
        if i == 0:
            ListOfVectors[0].y = randint(-10, 10)
        else:
            Value = Helper2()
            while Counter:
                if abs(Value - ListOfVectors[i-1].y) < 3:
                    ListOfVectors[i].y = Value
                    Counter = False
                else:
                    Value = Helper2()


    print(ListOfVectors)

AllVectors = []
for i in range(4):
    AllKVectors = []
    for k in range(4):
        AllKVectors.append(vec3d(i,0,k))
    AllVectors.append(AllKVectors)
    Helper(AllKVectors)
