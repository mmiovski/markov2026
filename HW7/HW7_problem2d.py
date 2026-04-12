import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

lam = 3
T = 48
lam_total = 2 * lam

# same arrival function as in part c
def simulate_hppp_times(lam, T):

    times = []
    t = 0.0
    
    while True:
        interarrival = np.random.exponential(scale=1/lam)
        t += interarrival
        if t > T:
            break
        times.append(t)
    
    return np.array(times)

# Simulate combined process, rate = 6
all_times = simulate_hppp_times(lam_total, T)

# Assign each basket to A or B with probability 1/2
labels = np.random.rand(len(all_times)) < 0.5

times_A = all_times[labels]
times_B = all_times[~labels]

# Plot
plt.figure(figsize=(12, 4))

plt.vlines(times_A, ymin=0.55, ymax=1.0, colors='red', label='Team A')
plt.vlines(times_B, ymin=0.0, ymax=0.45, colors='blue', label='Team B')

plt.xlim(0, T)
plt.ylim(-0.1, 1.1)
plt.xlabel("Time (minutes)")
plt.title("Simulated 48-minute Basketball Game (Single Combined Process)")
plt.yticks([])
plt.legend()
plt.grid(axis='x', alpha=0.3)

plt.show()