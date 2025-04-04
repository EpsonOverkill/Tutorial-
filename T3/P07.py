import tkinter as tk
from tkinter import messagebox
import math
def main():
    try:
        num = int(entry.get())
        if num < 0:
            raise ValueError("Negative number")
        result.set(f"Square Root: {math.sqrt(num):.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please input valid number.")
root = tk.Tk()
root.title("Square Root Calculator")
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Go", command=main).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()
root.mainloop()
