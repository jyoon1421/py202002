
n = int( input() )
if n<10 or n>50:
    n = int( input() )

from functools import reduce
def fact (n):
    result = reduce( lambda x,y: x*y, range(1, n+1) )
    return result

print( "{:,}".format( fact(n) ) )
