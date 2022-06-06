# Simulation of cell aggregate fusion

import numpy as np

from init.forces import relu_force
from init.solvers import take_euler_step
from init.making_sphere import sphere
from init.plotting_spheres import Plot_Sphere

import os
from progress.bar import FillingSquaresBar

# Parameters for Simulations
N = 85
T_relax = 5000
T = 10000
K = 5

R_agg= 5
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
sep=0.9

print("      Generating both spheres")
X=sphere(R_agg, N, R_cell,-sep*R_agg,0,0)

print("      Relaxing sphere")
bar = FillingSquaresBar(max = np.arange(start=0, stop=T_relax, step=dt).size)
for t in np.arange(start=0, stop=T_relax, step=dt):
    take_euler_step(X, N, dt, relu_force, r_max, s, K)
    bar.next()
bar.finish()

# Plotting Initial Conditions
Plot_Sphere(R_cell, X, 'data/NoMelt/N({})_RAgg({})_Init.vtk'.format(N,R_agg))

# Joining Spheres
Y=X+[2*sep*R_agg,0,0]
X = np.concatenate((X, Y), axis=0)

if MELTING == "yes":
    bar = FillingSquaresBar(max = np.arange(start=0, stop=T, step=dt).size)

    print("________________FUSING________________")
    print("Joining Spheres")
    # Plotting Initial Conditions
    os.mkdir('data/Melt/N({})_RAgg({})_T({})'.format(N,R_agg,T))
    Plot_Sphere(R_cell, X, 'data/Melt/N({})_RAgg({})_T({})/Init.vtk'.format(N,R_agg,T).format(N,R_agg))

    # Calculation of the time evolution of the system
    for t in np.arange(start=0, stop=T, step=dt):
        take_euler_step(X, 2*N, dt, relu_force, r_max, s, K)
        bar.next()
    bar.finish()
    # Plotting Final Conditions
    Plot_Sphere(R_cell, X ,'data/Melt/N({})_RAgg({})/Final.vtk'.format(N,R_agg))

if MELTING != "yes":
    # Plotting Final Conditions
    Plot_Sphere(R_cell, X, 'data/NoMelt/N({})_RAgg({})_Final.vtk'.format(N,R_agg))