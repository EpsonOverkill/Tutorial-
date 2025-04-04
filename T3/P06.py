import tkinter as tk
def convert_to_uppercase():
    input_text = input_entry.get()
    result_label.config(text=input_text.upper())
root = tk.Tk()
root.title("Uppercase Converter")
root.geometry("300x150")
tk.Label(root, text="Enter text:").pack(pady=5)
input_entry = tk.Entry(root)
input_entry.pack(pady=5)
tk.Button(root, text="Convert", command=convert_to_uppercase).pack(pady=5)
result_label = tk.Label(root, font=("Papyrus", 12, "bold"))
result_label.pack(pady=5)
root.mainloop()
