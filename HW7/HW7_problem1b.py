import numpy as np
import math
import matplotlib.pyplot as plt

# k = 30 since poisson probs past that are essentially 0
def p_tie(t, K=30):

    # initialize sum
    s = 0.0

    # define simplification of rate
    x = 1 - t/90

    # range between k = 1,...,30 (k = 0,...,29)
    for k in range(K + 1):

        # compute sum
        s += (3 * x**2)**k / (math.factorial(k)**2)

    # multiple by outside exponential
    return math.exp(-3.5 * x) * s

# 500 values between t = 0 and t = 90
t_vals = np.linspace(0, 90, 500)

# compute probability values for t = 0 to t = 90
p_vals = [p_tie(t) for t in t_vals]

# plot
plt.plot(t_vals, p_vals)
plt.xlabel("t")
plt.ylabel("P(Teams Tie| No Goals Up to Time t)")
plt.title("Probability the Game Ends in a Tie")
plt.grid(True)
plt.show()