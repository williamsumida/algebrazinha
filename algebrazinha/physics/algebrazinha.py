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
