
matrix_x = [[1,2,3],[4,5,6]]
matrix_y = [[1,2],[3,4],[5,6]]


def matrix_mul(*matrix):
    result =[ [sum(a*b for a,b in zip(row, column)) for column in zip(*matrix[1])] for row in matrix[0] ]

    if len(matrix) == 2:
        return result
    else:
        for i in range(2, len(matrix),1):
            return matrix_mul(result, matrix[i])

print( matrix_mul(matrix_x, matrix_y) )
