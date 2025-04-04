import tkinter as tk
l, num = 1, 200
guess = (l + num) // 2
def small():
    global l, guess
    l = guess + 1
    update()
def large():
    global num, guess
    num = guess - 1
    update()
def correct():
    result.set(f"Computer guessed it: {guess}")
def update():
    global guess
    guess = (l + num) // 2
    result.set(f"Is it {guess}?")
root = tk.Tk()
root.title("Computer Guesses Number")
result = tk.StringVar()
result.set(f"Is it {guess}?")
tk.Label(root, textvariable=result).pack()
tk.Button(root, text="Too Small, try again", command=small).pack()
tk.Button(root, text="Too Large, try again", command=large).pack()
tk.Button(root, text="Correct", command=correct).pack()
root.mainloop()
