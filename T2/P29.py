A, B = set(map(int, input("Enter set A: ").split())), set(map(int, input("Enter set B: ").split()))
print("Union:", A | B, "Intersection:", A & B, "Difference:", A - B)
