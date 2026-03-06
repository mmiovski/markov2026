import numpy as np
import matplotlib.pyplot as plt

# part a
pi_a = np.zeros(5)
pi_a[0] = 1.0
pi_a[1] = pi_a[0] * (p1 / q2)
pi_a[2] = pi_a[1] * (p2 / q3)
pi_a[3] = pi_a[2] * (p3 / q4)
pi_a[4] = pi_a[3] * (p4 / q5)

pi_a = pi_a / pi_a.sum()

# part b
pi_b = pi

# part c
pi_c = emp

states = np.arange(1, 6)
w = 0.25 # shift to show all 3

plt.bar(states - w, pi_a, width=w, label="Closed (A)", )
plt.bar(states,     pi_b, width=w, label="Numerical (B)")
plt.bar(states + w, pi_c, width=w, label="Empirical (C)")

plt.xticks(states)
plt.xlabel("State")
plt.ylabel("Probability")
plt.title("Empirical vs Theoretical Stationary Distributions")
plt.legend()
plt.show()