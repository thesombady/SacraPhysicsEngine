from random import randint
from SacraMathEngine import *

def MakeGroundPer(Vector):
    if not isinstance(Vector, vec3d):
        raise TypeError("[System]: Cannot compute value")
    else:
        Value = Vector[1]
        NewValue = randint(Value - 5, Value + 5)
        return NewValue
vector = vec3d(1,1,1)
for i in range(100):
    print(MakeGroundPer(vector))
