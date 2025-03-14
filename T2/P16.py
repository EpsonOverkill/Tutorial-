print("1: Even/Odd, 2: Pos/Neg/Zero, 3: Factors")
c = int(input("Enter choice: "))
if c == 1:
    n = int(input("Enter number: "))
    print("Even" if n % 2 == 0 else "Odd")
elif c == 2:
    n = int(input("Enter number: "))
    print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")
elif c == 3:
    n = int(input("Enter number: "))
    print("Factors:", [i for i in range(1, n+1) if n % i == 0])
