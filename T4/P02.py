class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = float(input("Enter length: "))
width = float(input("Enter width: "))
rect = Rectangle(length, width)
print("Area of Rectangle:", rect.area())
