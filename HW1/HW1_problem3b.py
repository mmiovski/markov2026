# libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# define f(u)
def f(u):
    return u**4 / (1 + u**6)

# true value found using numerical integration
I_true = quad(f, 0, 1)[0] # [0] grabs the estimate

# values of N
x_vals = np.arange(1, 5.1, 0.1)
N_vals = np.floor(10**x_vals).astype(int)

# initialize expected values list
E_vals = []

# monte carlo sim
for N in N_vals:
    U = np.random.rand(N)
    V = np.random.rand(N)
    below = V <= f(U)
    E_vals.append(np.mean(below))

# plot
plt.figure(figsize=(8, 5))
plt.plot(N_vals, E_vals, marker='o', linestyle='-', label='Monte Carlo Estimate E(N)')
plt.axhline(I_true, color='green', linestyle='--', label='True integral value')

plt.xscale('log') # log-scale on x-axis
plt.xlabel('N (log scale)') # label for x-axis
plt.ylabel('E(N)') # label for y-axis
plt.title('Monte Carlo Hit-or-Miss Estimate of Integral') # plot title
plt.legend() # plot legen
plt.grid(True, which='both', alpha=0.1) # plot grid

plt.show()