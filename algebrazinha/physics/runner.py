from algebrazinha import Algebrazinha
from vector import Vector

v1 = Vector(1.0, 2.3)
v2 = Vector(5.0, 3)

alg = Algebrazinha()

v_res = alg.sum_vectors(v1,v2)
print(v_res.x, v_res.y)
