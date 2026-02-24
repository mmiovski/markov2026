import random
import numpy as np
import math

# simulate game 100k times and return analytic E(M | XO = i)
def gamblers_ruin(i0 = 10, p = 0.35, q = 0.4, s = 0.25):
    i = i0
    while True:
        if i == 0:
            return 0  # ruined
        r = random.random()
        if r < s:
            return i  # retire with i dollars
        elif r < s + p:
            i += 1    # win $1
        else:
            i -= 1    # lost $1

vals = [gamblers_ruin() for _ in range(100000)]

# theoretical answer

# given values
p = 0.35
q = 0.40
s = 0.25
i = 10

# root from characteristic equation
r = (1 - math.sqrt(1 - 4*p*q)) / (2*p)

# theoretical expected final money
m_i = i + (p - q)/s * (1 - r**i)

print("Theoretical E[M|X0 = 10] =", round(m_i, 5))
print("Simulated mean:", round(np.mean(vals), 5))