import numpy as np
import time

# required number of accepted samples
N = 10**6

# accepted samples collection list initialization 
accepted = []

# optimal rejection c*
c = 4 / np.e

# proposal initialization
proposal = 0

# to track run time
start = time.time()

# need a while loop since we are collecting 10**6 accepted samples
while len(accepted) < N:
    
    proposal += 1

    # proposal, X ~ Exp(1/2)
    x = np.random.exponential(scale = 2)
    
    # uniform for acceptance test
    u = np.random.rand()
    
    # acceptance probability
    if u <= (np.e / 2) * x * np.exp(-x / 2):
        
        # add if true
        accepted.append(x)

end = time.time()

print("Runtime in Seconds:", round(end - start, 4))
print("Estimated Acceptance Rate", round(N / proposal, 4))