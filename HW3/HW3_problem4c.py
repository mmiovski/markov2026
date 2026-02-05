import numpy as np

# transition probabilities for states 1–6
P = {1: [1/2, 1/2, 0,   0,   0,   0],   # state 1
     2: [0,   1/2, 1/2, 0,   0,   0],   # state 2
     3: [1/3, 0,   1/3, 1/3, 0,   0],   # state 3
     4: [0,   0,   0,   1/2, 1/2, 0],   # state 4
     5: [0,   0,   0,   0,   0,   1],   # state 5
     6: [0,   0,   0,   0,   1,   0]}    # state 6

# number of times we simulate the 5 time steps
n_trials = 10000

# initialize success counter, success is X5 = 4 given X0 = 1
success = 0

# reprod. 
np.random.seed(42)

# _ because we are not tracking, just running 10K times
for _ in range(n_trials):
    
    # start in state 1, X0 = 1
    state = 1
    
    # simulate 5 steps
    for _ in range(5):

        # random choice selects the next state based on the row of probs for current state
        state = np.random.choice([1,2,3,4,5, 6], p=P[state])
    
    # check if X5 = 4
    if state == 4:
        success += 1

estimate = success / n_trials

print(f'Estimated probability of X5 = 4:', estimate)