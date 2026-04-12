import scipy.integrate as spi
import numpy as np

f = lambda t: np.exp(-0.5*t - t**3/5400)

result, error = spi.quad(f, 0, np.inf)

print("E[T] =", result)