string = input("Enter string: ")
print("Result:", ''.join(c for c in string if c.lower() not in 'aeiou'))
