class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"
comp1 = Complex(4,6)
comp2 = Complex(1,5)
comp3 = comp1 + comp2
print("Sum of complex numbers:", comp3)
