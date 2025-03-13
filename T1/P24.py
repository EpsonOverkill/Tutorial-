for num in range(100, 1001):
    if s(map(int, str(num))) % 9 == 0:
        print(num, end=" ")
print()
