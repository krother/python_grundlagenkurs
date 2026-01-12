from matplotlib import pyplot as plt

x = list(range(-10, 11))
y = [xx ** 2 for xx in x]

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("parabola.png")