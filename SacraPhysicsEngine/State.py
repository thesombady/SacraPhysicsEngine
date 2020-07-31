import sacramathengine

class StateError(Exceptions):
    pass


class State:

    ActiveMeshes = []

    def __init__(self):
        self.States = {
        "Solid" : "Solid",
        "NonSolid": "NonSolid"}
        #These should be functions...


    def _setter(self, state = None, Mesh = None):
        if state == None:
            raise StateError("[System]: Each object needs a state.")
        else:
            try:
                for key in self.States.keys():
                    if state == self.States(key):
                        self.state = self.States(key)
                    else:
                        pass
                    #Needs a small remake
            except:
                raise StateError("[System]: Cannot load a state for the object.")
            if Mesh == None:
                raise StateError("[System]: Each State-Object needs a mesh; Refer to SacraMathEngine.Mesh")
            else:
                if isinstance(Mesh, MeshObject): #Might need to rework that line
                    self.Mesh = Mesh
                    self.ActiveMeshes.append(self.Mesh)
                else:
                    raise StateError("[System]: State-Objects need MeshObjects as input in the _setter function")


    def _CenterOfMass(self):
        pass

    def _Collision(self, Other):
        pass

    def __str__(self):
        return f'{self.states}'

    def __repr__(self):
        return f'{self.states}'
