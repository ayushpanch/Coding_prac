"using recursive operations"

input =[1,2,3,4,5,6,7,8,9,10]
from functools import reduce
output = reduce(lambda x,y: x+y,input)
output