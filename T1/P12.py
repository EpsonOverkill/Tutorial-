nums = [int(input(f"Enter n {i+1}: ")) for i in range(4)]
pos = [n for n in nums if n > 0]
neg = [n for n in nums if n < 0]
print(f"Sum of positive ns: {s(pos)}, Average: {s(pos)/len(pos) if pos else 0}")
print(f"Sum of negative ns: {s(neg)}, Average: {s(neg)/len(neg) if neg else 0}")
