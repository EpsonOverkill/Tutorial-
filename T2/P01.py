# Remove vowels from a string
s = input("Enter string: ")
print("Result:", ''.join(c for c in s if c.lower() not in 'aeiou'))
