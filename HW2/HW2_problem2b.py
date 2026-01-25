import numpy as np
from scipy.optimize import newton # numerical root finder
import time # time tracker

# h(x) = F(x) - u
def h(x, u):
    return 1 - (x + 1) * np.exp(-x) - u

# h'(x) = xe**-x
def hprime(x, u):
    return x * np.exp(-x)

# invert the cdf using Newton's method
def invert_cdf(u):

    x0 = 1   # initial guess of x0 = 1 prevents h'(x0) = 0 and x0 > 0 so the domain remains valid
    
    return newton(h, x0 = x0, fprime = hprime, args = (u,)) # run Newton's method

# generate 10**6 U(0,1) samples
U = np.random.rand(10**6)

# track timing of numerical root finding
start = time.time()
X = np.array([invert_cdf(u) for u in U]) # find root for each u
end = time.time()

print("Runtime in Seconds:", round(end - start, 4))