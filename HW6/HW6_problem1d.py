import numpy as np
import matplotlib.pyplot as plt

# transition matrix
P = np.array([
    [0,   1,   0,   0,   0],
    [1/3, 0,   2/3, 0,   0],
    [0,   1/2, 0,   1/2, 0],
    [0,   0,   2/3, 0,   1/3],
    [0,   0,   0,   1,   0]
])

# initial distribution X0 = 2
q0 = np.array([0, 0, 1, 0, 0])

# q50 = q0*P**50
q50 = q0 @ np.linalg.matrix_power(P, 50)

# stationary distribution
pi = np.array([1/12, 1/4, 1/3, 1/4, 1/12])

# states
states = np.array([0, 1, 2, 3, 4])

# plot
plt.plot(states, q50, marker='o', label='q50(i)')
plt.plot(states, pi, marker='s', label='pi(i)')
plt.xlabel('i')
plt.ylabel('Probability')
plt.xticks(states)
plt.legend()
plt.show()

# print q50
print("q50 =", q50)
print("pi  =", pi)