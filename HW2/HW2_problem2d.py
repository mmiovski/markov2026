import numpy as np
import time

# number of required samples 
N = 10**6

# to track time
start = time.time()

# draw N samples from Y1 ~ Exponential(1)
Y1 = np.random.exponential(scale=1.0, size=N)

# draw N samples from Y2 ~ Exponential(1)
Y2 = np.random.exponential(scale=1.0, size=N)

# generate N samples for X ~ Gamma(2,1)
X = Y1 + Y2

end = time.time()

print("Runtime in Seconds:", round(end - start, 4))