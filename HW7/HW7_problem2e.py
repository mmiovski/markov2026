import numpy as np
from scipy.special import i0e

np.random.seed(42)

lam = 3
t = 48
n_games = 100000

# simulate total baskets
N = np.random.poisson(2 * lam * t, size = n_games) # Poisson(288)

# split baskets between A and B
N_A = np.random.binomial(N, 0.5)
N_B = N - N_A

# score difference
D = 2 * (N_A - N_B)

# simulation estimates
mean_est = np.mean(D)
var_est = np.var(D)
p_tie_est = np.mean(D == 0)

# theoretical values
mean_theory = 0
var_theory = 8 * lam * t # 1152
p_tie_theory = i0e(2 * lam * t) # since i0e(x) = exp(-x) I0(x), x>0

print("Estimated E[D(48)] =", mean_est)
print("Theoretical E[D(48)] =", mean_theory)
print("Estimated Var(D(48)) =", var_est)
print("Theoretical Var(D(48)) =", var_theory)
print("Estimated P(D(48)=0) =", p_tie_est)
print("Theoretical P(D(48)=0) =", p_tie_theory)