import numpy as np
import matplotlib.pyplot as plt

# theoretical solution from part (d)
def y1_theory(t):
    return 1/4 - (1/12)*np.exp(-2*t) + np.exp(-t)*((1/6)*np.cos(t) - (1/3)*np.sin(t))

# simulate N independent chains on a time grid
def simulate_fraction_in_state_1(N, t_grid):
    dt = t_grid[1] - t_grid[0]
    m = len(t_grid)

    # initial states: 1 with prob 1/3, 2 with prob 2/3
    initial_states = np.where(np.random.rand(N) < 1/3, 1, 2)

    # poisson increments for the jump process
    increments = np.random.poisson(dt, size=(N, m - 1))
    jump_counts = np.cumsum(increments, axis=1)
    jump_counts = np.hstack([np.zeros((N, 1), dtype=int), jump_counts])

    # state after k jumps from initial state
    states = ((initial_states[:, None] - 1 + jump_counts) % 4) + 1

    # fraction in state 1 at each time
    f_t = np.mean(states == 1, axis=0)
    return f_t

# time grid
t_grid = np.linspace(0, 5, 1001)
y_theory = y1_theory(t_grid)

# simulate and plot in a 2x2 grid
N_values = [100, 1000, 10000, 100000]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for ax, N in zip(axes, N_values):
    f_t = simulate_fraction_in_state_1(N, t_grid)
    ax.plot(t_grid, f_t, label=f"Simulated f(t), N={N}")
    ax.plot(t_grid, y_theory, label="Theoretical y1(t)")
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 0.5)
    ax.set_xlabel("t")
    ax.set_ylabel("Fraction in state 1")
    ax.set_title(f"Fraction in state 1 vs theory, N={N}")
    ax.legend()

plt.tight_layout()
plt.show()