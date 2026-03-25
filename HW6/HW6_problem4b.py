import numpy as np

# seed
np.random.seed(17)

# a = 0.49 is given
a = 0.49

# theoretical extinction probability as a function of a
if a < 0.5:
    phi = a / (1 - a)
else:
    phi = 1.0

print("Theoretical extinction probability =", np.round(phi, 5))

# simulation settings
n_sim = 1000  # 10^3
max_gens = 200

# simulate one branching process starting from X0 = 1
def simulate_avalanche(a, max_gens = 200):

    X = 1  # start with one particle

    for _ in range(1, max_gens):

        # Zn ~ Binomial(Xn, 1-a)
        Z = np.random.binomial(X, 1 - a)

        # X_{n+1} = 2*Zn
        X = 2 * Z

        if X == 0:
            return True  # extinct BEFORE generation 200

    return False

# run at least 1000 independent avalanches and count extinctions
extinct_count = 0

for _ in range(n_sim):

    if simulate_avalanche(a, max_gens):

        extinct_count += 1

# estimate extinction probability and compare to theory
phi_hat = extinct_count / n_sim

print("Estimated extinction probability =", np.round(phi_hat, 5))
print("Difference from theory =", np.round(abs(phi_hat - phi), 5))