# Find median
nums = sorted(map(int, input("Enter numbers: ").split()))
m = len(nums) // 2
print("Median:", nums[m] if len(nums) % 2 else (nums[m-1] + nums[m]) / 2)
