import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, label='Prime Numbers')

plt.title('Line Chart Example')

plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

plt.legend()

plt.show()