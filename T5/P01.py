def add(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
def trans(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
mat1 = [[1, 3, 5], [2, 4, 6]]
mat2 = [[9, 7, 5], [8, 6, 4]]
sum = add(mat1, mat2)
transpose = trans(sum)
print("Sum:", sum)
print("Transpose:", transpose)
