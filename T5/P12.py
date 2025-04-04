import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.figure(figsize=(8, 5))

plt.plot(x, y1, label='Multiples of 2', color='blue')
plt.plot(x, y2, label='Odd Numbers', color='red')      # Second line

plt.title('Two Lines on One Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')

plt.legend()
plt.show()
