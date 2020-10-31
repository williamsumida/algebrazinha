from vector import Vector
class Algebrazinha:

    def sum_vectors(self, vectors):
        x=0
        y=0
        z=0
        for vector in vectors:
            x += vector.x
            y += vector.y
            z += vector.z
        return Vector(x,y,z)

    def scale(self, vector, s):
        vector.x = vector.x * s
        vector.y = vector.y * s
        vector.z = vector.z * s
        return vector 
