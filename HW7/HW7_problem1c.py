import numpy as np
import math
import matplotlib.pyplot as plt


def p_tie_t60(t, K=30):

    # define simplification
    x = 1 - t/90

    # initialize sum
    s = 0.0

    # same loop as in part b 
    for k in range(K + 1):

        # new sum analytical soln
        s += (3 * x**2)**k / (math.factorial(k) * math.factorial(k + 1))

    # apply outside simplification
    return 1.5 * x * math.exp(-3.5 * x) * s


# from t = 60 to t = 90
t_vals = np.linspace(60, 90, 400)

# compute probs 
p_vals = [p_tie_t60(t) for t in t_vals]

# plot
plt.plot(t_vals, p_vals)
plt.xlabel("t")
plt.ylabel("P(Tie | A Score at 60, No Other Goals Up to Time t)")
plt.title("Probability Otis Wins the Bet")
plt.grid(True)
plt.show()