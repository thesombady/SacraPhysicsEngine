import sacramathengine
from math import sin, cos, tan, pi

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
                raise StateError("[System]: Each State-Object needs a mesh; Refer to SacraMathEngine.Mesh .")
            else:
                if isinstance(Mesh, MeshObject): #Might need to rework that line
                    self.Mesh = Mesh.Mesh
                    self.ActiveMeshes.append(self.Mesh)
                else:
                    raise StateError("[System]: State-Objects need MeshObjects as input in the _setter function.")
            try:
                self._CenterOfMass()
            except:
                raise StateError("[System]: Cannot compute center of mass, fault is in _setter method.")


    def _CenterOfMass(self):
        """A function that is called when using _setter method; Provides the center of mass of that mesh aswell as computing the largest offset."""
        if  isinstance(self.Mesh, (list, tuple)):
            try:
                Colletion = []
                for tri in self.Mesh:
                    CenterOfTriangle = 1/3 * (tri[0] + tri[1] + tri[2])
                    Collection.append(CenterOfTriangle)
                CenterOfMass = vec3d(0, 0, 0)
                for i in range(len(Collection)):
                    CenterOfMass += Collection[i]
                self.CenterOfMass = CenterOfMass / len(Collection)
                try:
                    def Maximum(*args):
                        for i in range(len(args)):
                            if not isinstance(args[i], Triangle):
                                raise TypeError("[System]: The input in Maximum function is not of correct format.")
                        MaxNorms = []
                        for tri in args:
                            vec1 = (self.CenterOfMass - tri[0]).norm()
                            vec2 = (self.CenterOfMass - tri[1]).norm()
                            vec3 = (self.CenterOfMass - tri[2]).norm()
                            NormsOfTri_i = [vec1, vec2, vec3]
                            MaxNorms.append(max(NormsOfTri_i))
                        self.MaxNorm = max(MaxNorms)

                    #compute the largest vector, then apply a rotation to that vector so it covers 360 degress around
                except:
                    raise StateError("[System]: Can't compute the radius")
            except:
                raise StateError("[System]: Can not compute center of mass.")
        else:
            raise TypeError("[System]: Can not load the center of mass, due to Type-Error of the mesh."):



    def _Collision(self, Other):
        try:
            if not isinstance(Other, state) and Other.state != "NonSolid":
                Epsilon = self.CenterOfMass - Other.CenterOfMass
                Delta = self.MaxNorm - Other.MaxNorm
                #Need to add __lq__ to vectors...
                if delta < 0 and ...:
                pass
            else:
                raise StateError("[System]: Can not compute _Collision method.")
        except:
            raise StateError("[System]: Can not compute _Collision method.")


    def __str__(self):
        return f'{self.state}'

    def __repr__(self):
        return f'{self.state}'
