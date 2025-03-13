# Check palindrome without reversing
s = input("Enter string: ")
print("Palindrome:", all(s[i] == s[-i-1] for i in range(len(s)//2)))
