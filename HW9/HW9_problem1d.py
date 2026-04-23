import numpy as np

alpha = 1
beta = 1
L = 20
N = 10000 # changed to 10K rather than 1K to get closer sample estimates

times = []

for _ in range(N):

    i = 0
    t = 0.0

    while i < L:

        if i == 0:
            wait = np.random.exponential(scale=1/alpha)
            t += wait
            i = 1

        else:
            wait = np.random.exponential(scale=1/(alpha + beta))
            t += wait

            if np.random.rand() < alpha / (alpha + beta):
                i += 1
            else:
                i -= 1

    times.append(t)

times = np.array(times)

sim_mean = np.mean(times)
sim_var = np.var(times, ddof=1)
theory = L * (L + 1) / (2 * alpha)

print("sim mean:", sim_mean)
print("theory mean:", theory)
print("sample var:", sim_var)