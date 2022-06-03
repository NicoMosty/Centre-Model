# Simulation of cell aggregate fusion

import numpy as np

from init.forces import relu_force
from init.solvers import take_euler_step
from init.making_sphere import sphere

import os
from progress.bar import FillingSquaresBar

# Modules for plotting spheres
from vedo import Spheres, interactive

# Parameters for Simulations
N = 30
T_relax = 5000
T = 30000
K = 1.5

R_agg= 3.5
R_cell = 1.0
r_max = 2.5 * R_cell
s = 1.8 * R_cell

dt = 0.1

os.system("cls")
print("_______FUSION OF CELL AGGREGATTES_______ \n")
MELTING=input("Do you want to simulate aggregate melting? \n(Write 'yes' if it requires spheroid fusion [Default: No]) \n" or "yes")
os.system("cls")

# Initialise cells
print("____________INIZIALIZATING____________")
sep=1

print("      Generating both spheres")
X=sphere(R_agg, N, R_cell,-sep*R_agg,0,0)

print("      Relaxing sphere")
bar = FillingSquaresBar(max = np.arange(start=0, stop=T_relax, step=dt).size)
for t in np.arange(start=0, stop=T_relax, step=dt):
    take_euler_step(X, N, dt, relu_force, r_max, s, K)
    bar.next()
bar.finish()

Y=X+[2*sep*R_agg,0,0]
print('Y=',Y.shape)
print('X=',X.shape)
# Joining Spheres
X = np.concatenate((X, Y), axis=0)
print('X=',X.shape)

if MELTING == "yes":
    bar = FillingSquaresBar(max = np.arange(start=0, stop=T, step=dt).size)

    print("________________FUSING________________")
    print("Joining Spheres")
    # Plotting Initial Conditions
    os.mkdir('data/Melt/N({})_RAgg({})_T({})'.format(N,R_agg,T))
    Spheres(X, c='b', r=R_cell).show(axes=1, interactive=0).screenshot('data/Melt/N({})_RAgg({})_T({})/Init.png'.format(N,R_agg,T))

    # Calculation of the time evolution of the system
    for t in np.arange(start=0, stop=T, step=dt):
        take_euler_step(X, 2*N, dt, relu_force, r_max, s, K)
        bar.next()
    bar.finish()
    # Plotting Final Conditions
    Spheres(X, c='b', r=R_cell).show(axes=1, interactive=0).screenshot('data/Melt/N({})_RAgg({})_T({})/Final.png'.format(N,R_agg,T))
    interactive()

if MELTING != "yes":
    # Plotting Final Conditions
    Spheres(X, c='b', r=R_cell).show(axes=1, interactive=0).screenshot('data/NoMelt/N({})_RAgg({}).png'.format(N,R_agg))
    interactive()