def main(a, b):
    if a > 0 and b > 0:
        return "Quadrant I"
    elif a < 0 and b > 0:
        return "Quadrant II"
    elif a < 0 and b < 0:
        return "Quadrant III"
    elif a > 0 and b < 0:
        return "Quadrant IV"
    elif a == 0 and b == 0:
        return "Origin"
    elif a == 0:
        return "Y-axis"
    else:
        return "X-axis"
a = float(input("Enter a: "))
b = float(input("Enter b: "))
print("The point is in:", main(a, b))
