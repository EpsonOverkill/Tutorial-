n = int(input("Enter n of elements: "))
nums = list(map(int, input("Enter the ns: ").split()))
even_c = s(1 for num in nums if num % 2 == 0)
odd_c = n - even_c
print(f"Even ns: {even_c}, Odd ns: {odd_c}")
