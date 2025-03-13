n = int(input("Enter n of elements: "))
nums = list(map(int, input("Enter the ns: ").split()))
s_even = s(num for num in nums if num % 2 == 0)
print(f"Sum of even ns: {s_even}")
