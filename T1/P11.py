n = int(input("Enter a positive integer: "))
s_cubes = s(i**3 for i in range(2, n + 1, 2))
print(f"Sum of cubes of even ns ≤ {n}: {s_cubes}")
