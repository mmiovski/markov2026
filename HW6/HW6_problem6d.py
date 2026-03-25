import numpy as np

# seed
np.random.seed(17)

# number of simulations
n_sim = 1000

# store avalanche sizes
sizes = []

# simulate 1000 avalanches
for _ in range(n_sim):
    X = 1          # start with one particle
    S = 0          # avalanche size
    
    while X > 0:

        S += X
        X = np.random.binomial(2 * X, 0.5)  # each particle has 0 or 2 children with prob 1/2
    
    sizes.append(S)

# estimated probability that S = 3
p3_est = np.mean(np.array(sizes) == 3)

# exact value from part (b): p3 = 1/8
p3_exact = 1 / 8

# print results
print("Estimated P(S=3) =", p3_est)
print("Exact p3 =", p3_exact)
print("Difference =", abs(p3_est - p3_exact))