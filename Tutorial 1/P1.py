sec = int(input("Enter time in seconds: "))
hrs = sec//3600
min = (sec%3600)//60
sec = sec%60
print(f"{hrs:02}:{min:02}:{sec:02}")
