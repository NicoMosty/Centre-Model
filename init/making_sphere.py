import numpy as np
from math import pi
from numpy import sin,cos
from progress.bar import FillingSquaresBar


def coord_sph(R_agg,x_o,y_o,z_o):
    theta=np.random.uniform(low=0, high=pi, size=1)
    fi=np.random.uniform(low=0, high=2*pi, size=1)
    radius=np.random.uniform(low=0, high=R_agg, size=1)

    x = radius*sin(theta)*cos(fi)+x_o
    y = radius*sin(theta)*sin(fi)+y_o
    z = radius*cos(theta)+z_o

    return np.column_stack((x, y, z))

def sphere(R_agg, N, r_cell,x_o,y_o,z_o):
    bar = FillingSquaresBar(max = N)
    X=coord_sph(R_agg,x_o,y_o,z_o)
    for n in range(N):
        while True:
            X_n = coord_sph(R_agg,x_o,y_o,z_o)
            for i in range(X.shape[0]):
                r = X[i] - X_n[0]
                dist = np.linalg.norm(r)
                if dist < 1.8*r_cell:
                    X_n = np.column_stack((0,0,0))
                    break
            if np.linalg.norm(X_n) == 0:
                continue
            else:
                X = np.concatenate((X, X_n), axis=0)
                break
        bar.next()
    bar.finish()
    return X