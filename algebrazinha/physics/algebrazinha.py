from vector import Vector
class Algebrazinha:

    def sum_vectors(self, v1, v2):
        x = v1.x + v2.x
        y = v1.y + v2.y
        z = v1.z + v2.z
        return Vector(x,y,z)
