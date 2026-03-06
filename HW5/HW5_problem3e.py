import numpy as np
import matplotlib.pyplot as plt

def build_P(a: float) -> np.ndarray:
    return np.array([
        [1-a, a,   0.0],
        [a,   0.0, 1-a],
        [0.0, 1-a, a  ]
    ], dtype=float)

def theoretical_qn1(P: np.ndarray, n_max: int) -> np.ndarray:
    # q_{n+1} = q_n P, starting q0 = [1,0,0]
    q = np.array([1.0, 0.0, 0.0], dtype=float)
    out = np.empty(n_max + 1, dtype=float)
    out[0] = q[0]  # probability of state 1 at time 0
    for n in range(1, n_max + 1):
        q = q @ P
        out[n] = q[0]
    return out

def simulate_fn(P: np.ndarray, N: int, n_max: int, seed: int = 0) -> np.ndarray:
    """
    Simulate N independent chains, all starting in state 1 (index 0).
    Returns f_n for n=0..n_max.
    """
    rng = np.random.default_rng(seed)

    # states encoded as 0,1,2 corresponding to {1,2,3}
    states = np.zeros(N, dtype=np.int64)

    # cumulative transition probs for each current state
    cdf = np.cumsum(P, axis=1)  # shape (3,3), rows end at 1

    fn = np.empty(n_max + 1, dtype=float)
    fn[0] = 1.0  # all start in state 1

    for n in range(1, n_max + 1):
        u = rng.random(N)

        c = cdf[states]  # shape (N,3): row per chain given its current state
        # next state is first index where u <= cdf
        states = (u[:, None] > c).sum(axis=1)

        fn[n] = (states == 0).mean()

    return fn

def main():
    a = 0.99
    n_max = 300
    P = build_P(a)

    # theory
    q1_theory = theoretical_qn1(P, n_max)

    # empirics
    Ns = [100, 1000, 10000]
    f_curves = {}
    for i, N in enumerate(Ns):
        f_curves[N] = simulate_fn(P, N, n_max, seed=123 + i)

    # plot
    n = np.arange(n_max + 1)

    plt.figure(figsize=(8,5))

    # theoretical curve
    plt.plot(n, q1_theory, color="black", linewidth=3, label="Theory $q_n(1)$")

    # empirical curves
    plt.plot(n, f_curves[100],   color="orange", alpha=0.4, label="Empirical (N=100)")
    plt.plot(n, f_curves[1000],  color="green",  alpha=0.5, label="Empirical (N=1000)")
    plt.plot(n, f_curves[10000], color="red",    alpha=0.6, label="Empirical (N=10000)")

    # stationary distribution line
    plt.axhline(1/3, linestyle="--", color="gray", label=r"$\pi_1=1/3$")

    plt.xlabel("n")
    plt.ylabel("Probability of state 1")
    plt.title("Convergence to Stationarity (a = 0.99)")
    plt.ylim(0.1,0.5)

    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()