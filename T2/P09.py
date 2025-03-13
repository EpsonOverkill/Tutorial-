# Reverse first and second halves
s = input("Enter string: ")
m = len(s) // 2
print("Result:", s[:m][::-1] + s[m:][::-1])
