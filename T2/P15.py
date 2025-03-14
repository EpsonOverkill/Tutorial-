def f(n): return 1 if n == 0 else n * f(n-1)
n, r = map(int, input("Enter n, r: ").split())
print("nCr:", f(n) // (f(r) * f(n - r)))
