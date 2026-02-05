import numpy as np

p = np.array([[0.9, 0.1, 0.0],
              [0.0, 0.875, 0.125],
              [0.4, 0.0, 0.6]])

# p ** 50
p50 = np.linalg.matrix_power(p, 50)

# print, rounded to five decimals
print(np.round(p50, 5))