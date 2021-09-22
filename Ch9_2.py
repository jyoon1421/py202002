def scalar_vector_product(scalar_v,*vector_list):
    return [scalar_v*t for t in vector_list]

print( scalar_vector_product(5, *[1,3,5,7,11,13]) )
