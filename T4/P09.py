class Rectangle:
    def __init__(self, h, w, xcorner, ycorner):
        self.height = h
        self.width = w
        self.xcorner = xcorner
        self.ycorner = ycorner
    def center(self):
        xcenter = self.xcorner + self.width / 2
        ycenter = self.ycorner + self.height / 2
        return (xcenter, ycenter)
    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)
rec = Rectangle(5, 2, 3, 1)
print("Center:", rec.center())
print("Area:", rec.area())
print("Perimeter:", rec.perimeter())
