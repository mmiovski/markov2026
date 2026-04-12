import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# rate function
def lam(t):
    return 0.5 * (1 + (t / 30)**2)

# set time span and maximum rate on [0, 120]
T = 120
lambda_max = lam(T)

# sample candidate arrival times from a HPPP with rate lambda_max
candidate_times = []
t = 0.0

while True:

    # generate the next interarrival time
    interarrival = np.random.exponential(scale=1 / lambda_max)
    t += interarrival
    
    # stop if the next arrival is beyond day 120
    if t > T:
        break
    
    candidate_times.append(t)

candidate_times = np.array(candidate_times)

# Keep each candidate time Ti with probability lam(Ti) / lambda_max
report_times = []

for ti in candidate_times:

    keep_prob = lam(ti) / lambda_max

    u = np.random.uniform(0, 1)
    
    if u <= keep_prob:
        report_times.append(ti)

report_times = np.array(report_times)

# plot histogram of report times per day for days 0 to 120
plt.hist(report_times, bins=np.arange(0, 122, 1), edgecolor='black')
plt.xlim(0, 120)
plt.xlabel('Day')
plt.ylabel('Number of reports')
plt.title('Histogram of report times per day')
plt.show()

# compare the total number of reports with the expected value from part (b)
print("Total number of reports:", len(report_times))
print("Expected value from part (b):", 380)