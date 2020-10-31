from algebrazinha import Algebrazinha
from vector import Vector

v1 = Vector(1.0, 2.3)
v2 = Vector(5.0, 3)

algebrazinha = Algebrazinha()

v_res = algebrazinha.sum_vectors([v1,v2])
print(v1.x, v1.y)
print(v2.x, v2.y)
print(v_res.x, v_res.y)
