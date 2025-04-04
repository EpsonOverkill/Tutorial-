str = input("Enter string: ")
print("Palindrome:", all(s[i] == str[-i-1] for i in range(len(s)//2)))
