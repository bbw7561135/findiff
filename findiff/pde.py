from itertools import product
import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import spsolve


class PDE(object):

    def __init__(self, lhs, rhs, bcs):
        self.lhs = lhs
        self.rhs = rhs
        self.bcs = bcs

    def solve(self, shape):

        self._L = self.lhs.matrix(shape) # expensive operation, so cache it
        L = sparse.lil_matrix(self._L)
        f = self.rhs.reshape(-1)

        for key, val in self.bcs.items():
            L[key, :] = 0
            L[key, key] = 1
            f[key] = val

        print(L.toarray())
        print(f)

        L = sparse.csr_matrix(L)
        return spsolve(L, f)
