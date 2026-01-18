import numpy as np
import matplotlib.pyplot as plt

# num sims
N = 10**5

# simulate arrivals on Unif(6,7) (N rows, 3 cols)
arrivals = np.random.uniform(6, 7, size=(N, 3))

# T = max arrival time
T = np.max(arrivals, axis=1) # axis = 1 for row-wise max

# theoretical pdf derived in part (a)
t_vals = np.linspace(6, 7, 500) # 500 points
pdf_vals = 3 * (t_vals - 6)**2 # theoretical pdf

# plot
plt.figure(figsize=(8, 5))

# histogram as density
plt.hist(T, bins=100, density=True, alpha=0.6, label="Simulated T")

# theoretical curve
plt.plot(t_vals, pdf_vals, 'r', lw=2, label="Theoretical PDF")

plt.xlabel("t") # x label
plt.ylabel("Density") # y label
plt.title("Simulation vs Theoretical PDF of T") # main title
plt.legend() # legend
plt.show()