low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
s_odds = s(i for i in range(low, high + 1) if i % 2 != 0)
print(f"Sum of odd ns: {s_odds}")
