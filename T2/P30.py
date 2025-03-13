# Remove all duplicates
from collections import Counter
nums = list(map(int, input("Enter numbers: ").split()))
c = Counter(nums)
print("Result:", [n for n in nums if c[n] == 1])
