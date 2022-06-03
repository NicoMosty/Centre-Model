from stat import FILE_ATTRIBUTE_ARCHIVE
import numpy as np
from numba import njit, prange
from math import cos, sin, acos, atan2, pow


@njit(parallel=True)
def relu_force(X, n, r_max, s, K):

    # Initialise displacement array
    dX = np.zeros(shape=(n, X.shape[1]))

    # Loop over all cells to compute displacements
    for i in prange(n):

        # Initialise variables
        Xi = X[i,:]

        # Scan neighbours
        for j in range(n):
            if i != j :
                r = Xi - X[j,:]
                dist = np.linalg.norm(r)
                # Calculate attraction/repulsion force differential here
                if dist < r_max:
                    F = - K*(dist - r_max)**2*(dist - s)
                    dX[i,:] += r * F /dist
            
    return dX