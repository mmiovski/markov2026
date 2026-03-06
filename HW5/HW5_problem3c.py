import sympy as sp

# define symbol
a = sp.symbols('a')

# transition matrix
P = sp.Matrix([
    [1-a, a, 0],
    [a, 0, 1-a],
    [0, 1-a, a]
])

# plug in a = 0.99
a_val = 0.99
A = P.subs(a, a_val)

# eigenvalues and eigenvectors
eigs = A.eigenvects()

# extract eigenvalues
lam1 = eigs[1][0]   # eigenvalue ≈ 1
lam2 = eigs[0][0]
lam3 = eigs[2][0]

# extract eigenvectors
eps1 = eigs[1][2][0]
eps2 = eigs[0][2][0]
eps3 = eigs[2][2][0]

# initial distribution (X0 = 1)
q0 = sp.Matrix([1,0,0])

# build eigenvector matrix
E = sp.Matrix.hstack(eps1, eps2, eps3)

# solve q0 = c1eps1 + c2eps2 + c3eps2
c = E.LUsolve(q0)
c1, c2, c3 = c

# construct q_n^T
n = sp.symbols('n')
qn = c1*(lam1**n)*eps1 + c2*(lam2**n)*eps2 + c3*(lam3**n)*eps3

# stationary distribution
pi = sp.Matrix([sp.Rational(1,3), sp.Rational(1,3), sp.Rational(1,3)])

print("Stationary distribution:")
sp.pprint(pi)

# show decay of eigenvalue powers (exponential convergence)
n_pos = sp.symbols('n', positive=True)

decay2 = sp.Abs(lam2)**n_pos
decay3 = sp.Abs(lam3)**n_pos

print("\nDecay terms:")
sp.pprint(decay2)
sp.pprint(decay3)

print("\nLimits of decay terms as n goes to infinity:")
print("limit |Lam2|^n =", sp.limit(decay2, n_pos, sp.oo))
print("limit |Lam3|^n =", sp.limit(decay3, n_pos, sp.oo))