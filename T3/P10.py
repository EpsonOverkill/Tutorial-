import tkinter as tk
def main():
    height = float(height.get())
    breadth = float(bounce.get())
    count = int(count.get())
    dist = height
    for _ in range(count):
        height *= breadth
        dist += 2 * height
    result.set(f"Total Distance: {dist:.2f}")
root = tk.Tk()
root.title("Distance")
tk.Label(root, text="Height").pack()
height = tk.Entry(root)
height.pack()
tk.Label(root, text="Bounciness Index").pack()
bounce = tk.Entry(root)
bounce.pack()
tk.Label(root, text="Bounces").pack()
count = tk.Entry(root)
count.pack()
tk.Button(root, text="Calculate", command=main).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()
root.mainloop()
