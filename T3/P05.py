import turtle
t = turtle.Turtle()
t.speed(2)
def hexa(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)
for _ in range(10):
    hexa(150)
    t.right(36)
