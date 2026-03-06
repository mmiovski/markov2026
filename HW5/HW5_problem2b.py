import numpy as np

a = 0.04
b = 0.16
K = 0.1

# pn = K*e**(a*n)
p1 = K*np.exp(a * 1)
p2 = K*np.exp(a * 2)
p3 = K*np.exp(a * 3)
p4 = K*np.exp(a * 4)

# qn = K*e**(b*(n-1))
q2 = K*np.exp(b * (2-1))
q3 = K*np.exp(b * (3-1))
q4 = K*np.exp(b * (4-1))
q5 = K*np.exp(b * (5-1))

# P matrix
P = np.array([[1-p1, p1, 0, 0, 0],
              [q2, 1-p2-q2, p2, 0, 0],
              [0, q3, 1-p3-q3, p3, 0],
              [0, 0, q4, 1-p4-q4, p4],
              [0, 0, 0, q5, 1-q5]])

# transpose
P_T = P.T

# get e-vectors and e-values from P_T
e_val, e_vec = np.linalg.eig(P_T)

# print(e_val) # shows e_val = 1 is index 3

# get corresponding e_vec
v = np.real(e_vec[:, 3])

pi = v / v.sum() # divide by sum of v to normalize

print(pi)
# print(pi @ P) # confirmation