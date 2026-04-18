import sympy as sp

# state order: [F, N, D]
Q = sp.Matrix([
    [-2,  1,  1],
    [ 1, -1,  0],
    [ 1,  0, -1]])

# eigenvalues with multiplicities
eigs = Q.eigenvals()
print("eigenvalues:", eigs)