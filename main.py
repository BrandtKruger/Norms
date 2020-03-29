import sys
import numpy as np

from numpy import linalg

# define an array
A = np.arange(9) - 3
print(A)

B = A.reshape((3,3))
print("\n",B)
print("\n")

# Euclidean (L2) norm - default
print(np.linalg.norm(A))
print(np.linalg.norm(B))

# the Frogenius norm is the L2  norm for a matrix
print(np.linalg.norm(B, 'fro'))

# the max norm (P = infinity)
print(np.linalg.norm(A, np.inf))
print(np.linalg.norm(B, np.inf))

# vector normalization - normalization to produce a unit vector
norm = np.linalg.norm(A)
A_unit = A / norm
print(A_unit)

# the magnitude of a unit vector is equal to 1
print(np.linalg.norm(A_unit))


