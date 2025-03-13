x = int(input("Enter base: "))
y = int(input("Enter exponent: "))
res = 1
for _ in range(y):
    res *= x
print(f"{x}^{y} = {res}")
