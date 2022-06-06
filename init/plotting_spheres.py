import pyvista
import numpy as np

def Plot_Sphere(r,X,saved):
    j=0
    for i in X:
        if j == 0:
            merged = pyvista.Sphere(radius = r, center=i)
        if j != 0:
            sphere = pyvista.Sphere(radius = r, center=i)
            merged = merged.merge([sphere])
        j = j + 1
    merged.save(saved)
    merged.plot()
    