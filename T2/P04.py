s = input("Enter string: ")
print("Result:", s.replace(" ", "or") if " " in s else "S" + s + "S")
