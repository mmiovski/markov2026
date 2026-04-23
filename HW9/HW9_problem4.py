import math
import matplotlib.pyplot as plt

# setting beta = 1 (note not given beta in the question, so choose simplest)
beta = 1

m_values = list(range(10, 100001, 500))

stochastic_values = [(1 / beta) * sum(1 / k for k in range(1, m)) for m in m_values]


deterministic_values = [math.log(m) / beta for m in m_values]

plt.figure(figsize=(8, 5))
plt.plot(m_values, stochastic_values, label="stochastic E[tau_m]")
plt.plot(m_values, deterministic_values, label="deterministic ln(m)/beta")

plt.xlabel("m")
plt.ylabel("Time")
plt.title("Stochastic expected hitting time vs Deterministic hitting time")
plt.legend()
plt.grid(True)
plt.show()