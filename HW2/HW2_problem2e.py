import numpy as np
import matplotlib.pyplot as plt

# NOTE: the method I am using is part (d), sum of exponentials
# NOTE: X is defined in the part (d) code as X = Y1 + Y2
# where Y1, Y2 ~ Exponential(1)

# theoretical pdf
def gamma_pdf(x):
    return x * np.exp(-x)

# x-grid for pdf
x_vals = np.linspace(0, np.max(X), 1000)

# plot histogram (normalized)
plt.hist(X, 
         bins = 75, 
         density = True, 
         alpha = 0.5, 
         label = "Sample Histogram")

# overlay theoretical pdf
plt.plot(x_vals, 
         gamma_pdf(x_vals), 
         'k-', 
         lw=1, 
         label="Theoretical PDF")

plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.title("Histogram of Samples from Part (d) with Theoretical PDF Overlay")
plt.show()