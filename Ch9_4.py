def vector_sub(*vector):
    return[t[0]*2-sum(t) for t in zip(*vector)]

print( vector_sub([1,3],[2,4]) )
print( vector_sub([1,5],[10,4],[4,7]) )
print( vector_sub([10,9,8],[1,2,3],[3,4,5],[1,1,1]) )
    
