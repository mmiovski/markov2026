import numpy as np

# label the states numerically
# 0 = G (Growing)
# 1 = S (Synthesizing DNA)
# 2 = D (Dividing)

# transition probability matrix
# P[current_state] gives a list of probabilities for going to [G, S, D]
P = {0: [0.9,   0.1,   0.0],    # from G: stay in G w.p. 0.9, go to S w.p. 0.1
     1: [0.0,   0.875, 0.125],  # from S: stay in S w.p. 0.875, go to D w.p. 0.125
     2: [0.4,   0.0,   0.6]}     # from D: go to G w.p. 0.4, stay in D w.p. 0.6


n_steps = 10_000      # total number of steps (hours) to simulate
state = 0             # start the process in state G
counts = np.zeros(3)  # counts[i] will store how many times we visit state i

# random seed for reproducibility
np.random.seed(42)

# loop over time steps
for _ in range(n_steps): # _ because we only care about looping 10K times
    
    # add 1 to the count of the current state
    counts[state] += 1
    
    # randomly choose next state depending on current state and transition probabilities
    state = np.random.choice([0, 1, 2],      # possible next states: G, S, D
                              p=P[state])    # transition probabilities depend on the current state

    

# after the sim, divide counts by total steps to get the fraction of time spent in each state
fractions = counts / n_steps

# print fractions
fractions