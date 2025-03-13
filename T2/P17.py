# Factorial using recursion
def f(n): return 1 if n == 0 else n * f(n-1)
n = int(input("Enter number: "))
print("Factorial:", f(n))
