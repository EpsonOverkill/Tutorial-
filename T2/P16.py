# Compute sin(x) series
import math
x, n = map(float, input("Enter x, n: ").split())
x = math.radians(x)
print("sin(x):", sum(((-1)**i * x**(2*i+1) / math.factorial(2*i+1)) for i in range(int(n))))
