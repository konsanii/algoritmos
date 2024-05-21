from functools import reduce
from operator import mul

ra=[3,0,1,1,3,9,2,4,1,3,0,4,6]
somar = sum(ra)
print(somar)


multiplicar = reduce(mul, ra, 1)
print(multiplicar)