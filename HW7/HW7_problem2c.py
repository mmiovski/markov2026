import numpy as np
import matplotlib.pyplot as plt

# reproducibility
np.random.seed(42)

lam = 3          # rate per minute
T = 48           # total game length in minutes

# simulate interarrivals function
def simulate_hppp_times(lam, T):

    # initialize times and start at t = 0
    times = []
    t = 0.0
    
    
    while True:

        # define interarrival times
        interarrival = np.random.exponential(scale=1/lam)

        # accumulate interarrival times
        t += interarrival

        # stop at t = 48
        if t > T:

            break

        times.append(t)
    
    return np.array(times)

# Simulate basket times for each team
times_A = simulate_hppp_times(lam, T)
times_B = simulate_hppp_times(lam, T)

# Plot vertical bars
plt.figure(figsize=(12, 4))

# A = red and B = blue
plt.vlines(times_A, ymin=0.55, ymax=1.0, colors='red', label='Team A')
plt.vlines(times_B, ymin=0.0, ymax=0.45, colors='blue', label='Team B')

plt.xlim(0, T)
plt.ylim(-0.1, 1.1)
plt.xlabel("Time (min.)")
plt.title("Simulated 48 min. Basketball Game")
plt.yticks([])
plt.legend()
plt.grid(axis='x', alpha=0.3)

plt.show()