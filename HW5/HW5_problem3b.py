# for eigenvalues as a function of a
import sympy as sp

a = sp.symbols('a')

P = sp.Matrix([[1-a, a, 0],
               [a, 0, 1-a],
               [0, 1-a, a]])

# P = Ptranspose = A
P_T = P


# eigenvalues
P_T.eigenvals()

# eigenvectors
P_T.eigenvects()