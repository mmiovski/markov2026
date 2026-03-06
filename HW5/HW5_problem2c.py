import numpy as np
import matplotlib.pyplot as plt

T = 10**6
states = np.arange(5)          # 0,1,...,4 corresponds to states 1,2,...,5
x = 0                          # start at state 1 (index 0)
counts = np.zeros(5)

# compute cumulative probs for faster sampling
cumP = np.cumsum(P, axis=1)

# seed for reproducibility
np.random.default_rng(17)

for _ in range(T):
    u = np.random.uniform(0,1)  # sample from (0,1)
    x = np.searchsorted(cumP[x], u)  # next state index
    counts[x] += 1 # count how many times state is visited

emp = counts / T # normalize

plt.bar(np.arange(1, 6), emp)
plt.xticks(np.arange(1, 6))
plt.xlabel("State")
plt.ylabel("Fraction of Time Visited")
plt.title(f"Number of Times Visited Over T={T:,} Steps")
plt.show()