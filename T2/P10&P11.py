import re
p = input("Enter password: ")
print("Valid" if len(p) >= 6 and re.search(r'[a-z]', p) and re.search(r'[A-Z]', p) and re.search(r'\d', p) and re.search(r'[$#@]', p) else "Invalid")
