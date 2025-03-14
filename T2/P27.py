def is_p(n): return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
nums = list(map(int, input("Enter numbers: ").split()))
print("Primes:", [n for n in nums if is_p(n)], "Composites:", [n for n in nums if not is_p(n)])
