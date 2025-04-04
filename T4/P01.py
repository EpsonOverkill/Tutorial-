class Arith:
    def read(self):
        self.n1 = float(input("num1: "))
        self.n2 = float(input("num2: "))
    def add(self):
        return self.n1 + self.n2
obj = Arith()
obj.read()
print("Sum:", obj.add())
