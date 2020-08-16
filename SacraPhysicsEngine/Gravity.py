from .State import State

global FPS

class Gravity:
    GravityPull = 9.82
    def __init__(self):
        pass

    def _setter(self, Object = None):
        if Object == None:
            raise TypeError("[System]: Gravity must have an object")
        elif is not isinstance(Object, State):
            raise TypeError("[System]: Gravity must have an State-object")
        else:
            self.CenterOfMass =

    def __str__(self):
        return f'{None}'


Gravity(60)
