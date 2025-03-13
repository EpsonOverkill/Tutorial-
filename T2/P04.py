# Replace spaces with 'or', else add 'S' at ends
s = input("Enter string: ")
print("Result:", s.replace(" ", "or") if " " in s else "S" + s + "S")
