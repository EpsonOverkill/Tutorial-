import numpy as np

mat1 = np.random.randint(0, 20, (3, 3))
mat2 = np.random.randint(0, 20, (3, 3))

print("Matrix 1:")
print(mat1)
print("\nMatrix 2:")
print(mat2)

addition = mat1 + mat2
print("\nMatrix Addition:")
print(addition)

multiplication = np.dot(mat1, mat2)
print("\nMatrix Multiplication:")
print(multiplication)

transpose = multiplication.T
print("\nTranspose of Product Matrix:")
print(transpose)
