num = int(input("Enter a n: "))
n = len(str(num))
s_digits = s(int(digit) ** n for digit in str(num))
print(f"{num} is an Armstrong n" if s_digits == num else f"{num} is not an Armstrong n")
