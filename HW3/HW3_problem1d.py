import numpy as np
import matplotlib.pyplot as plt

# x-axis values
x = np.linspace(0, 10, 1000)

# f(x)
f = (1/3) * x * (1 + x) *  np.exp(-x)

# a*
astar = np.sqrt(3) - 1

# c(a*) * g_a*_(x)
cg_astar = (x * np.exp(-astar*(x + 1))) / (3 * (1 - astar))

# plot
plt.figure(figsize=(7, 7))
plt.plot(x, f, label='f(x)')
plt.plot(x, cg_astar, label='c(a*) * g_a*_(x)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()