col, row = input().split()
col = int(col)
row = int(row)
matrix = []

for i in range(row):
    matrix.append(list(input()))
print()
for i in range(row):
    for j in range(col):
        count = 0
        if matrix[i][j] == '.':
            if i != 0 and j != 0:
                if matrix[i-1][j-1] == '*':
                    count += 1
            if i != row-1 and j != col-1:
                if matrix[i+1][j+1] == '*':
                    count += 1
            if i != 0:
                if matrix[i-1][j] == '*':
                    count += 1
            if i != 0 and j != col-1:
                if matrix[i-1][j+1] == '*':
                    count += 1
            if j != 0:
                if matrix[i][j-1] == '*':
                    count += 1
            if i != row-1 and j != 0:
                if matrix[i+1][j-1] == '*':
                    count += 1
            if j != col-1:
                if matrix[i][j+1] == '*':
                    count += 1
            if i != row -1:
                if matrix[i+1][j] == '*':
                    count += 1
            matrix[i][j] = count
            print(matrix[i][j], end = "")
        else:
            print(matrix[i][j], end = "")
    print()
