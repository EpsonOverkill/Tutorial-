# Separate ints, floats, and strings
d = input("Enter values: ").split()
i, f, s = [int(x) for x in d if x.isdigit()], [float(x) for x in d if '.' in x], [x for x in d if not x.replace('.', '').isdigit()]
print("Ints:", i, "Floats:", f, "Strings:", s)
