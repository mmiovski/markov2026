import numpy as np
import matplotlib.pyplot as plt

# parameters
gamma = 4
x0 = 10

# sample sizes
Ns = [100, 1000, 10000]

# inverse transform sampler function
def sample_power_law(n, x0, gamma):
    U = np.random.uniform(0, 1, size=n)    # draw n samples of U(0,1)
    X = x0 * (1 - U) ** (-1 / (gamma - 1)) # set X equal to the inverse
    return X

# theoretical pdf function
def theoretical_pdf(x, x0, gamma):
    return (gamma - 1) * x0**(gamma - 1) * x**(-gamma)

# x-axis values for plotting
x_vals = np.linspace(x0, 60, 1000) # generate 1000 x values from x0 to 60
pdf_vals = theoretical_pdf(x_vals, x0, gamma) # compute theoretical pdf using those x values

# plot
plt.figure(figsize=(8, 6))

for N in Ns:
    
    samples = sample_power_law(N, x0, gamma) # apply inverse transform sampler function
    
    # generate plot
    plt.hist(samples,
             range = (x0, 60),
             bins = 50,
             density = True, # normalize to area 1
             alpha = 0.35,
             label = f"N = {N}")

# overlay theoretical pdf
plt.plot(x_vals, pdf_vals, 'k-', lw=1, label="Theoretical PDF")

plt.xlim(0, 60) # bound to x contained in [0, 60]
plt.xlabel("x")
plt.ylabel("Density")
plt.title("Sampling Power-Law Distribution Using Inverse Transform")
plt.legend()
plt.show()