from collections import Counter
nums = list(map(int, input("Enter numbers: ").split()))
print("Mode:", Counter(nums).most_common(1)[0][0])
