import numpy as np
import matplotlib.pyplot as plt

# number of monte carlo samples per n
m = 10**6

# values of n = 2**k for k = 2,...,10
k_vals = np.arange(2, 11)
n_vals = 2 ** k_vals

skew_estimates = []
skew_theory = []

for n in n_vals:

    # NOTE: we draw T ~ poisson(n) because if X_1,...,X_n ~ i.i.d poisson(1),
    # then their sum T_n = X_1 + ... + X_n ~ poisson(n)
    # REASON: this avoids simulating n poisson(1) variables each time, thereby
    # saving computational cost

    T = np.random.poisson(lam=n, size=m)

    # construct Y_n = (T_n - n) / sqrt(n)
    Y = (T - n) / np.sqrt(n)

    # sample mean
    Y_bar = np.mean(Y)

    # sample var
    var_hat = np.mean((Y - Y_bar)**2)

    # sample skew (plug-in estimator)
    skew_hat = np.mean((Y - Y_bar)**3) / (var_hat ** (3/2))

    skew_estimates.append(skew_hat)       # skew estimates
    skew_theory.append(1 / np.sqrt(n))    # theoretical skew with n points

# plot (log-log scale)
plt.figure()
plt.loglog(n_vals, skew_estimates, 'o-', label='Estimated skewness')
plt.loglog(n_vals, skew_theory, 'r--', label='Theoretical 1/sqrt(n)')
plt.xlabel('n')
plt.ylabel('Skewness')
plt.legend()
plt.show()