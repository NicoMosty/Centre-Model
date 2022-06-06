# Centre Model for Fusing Cell Aggregates

A Python implementation of some of the parallel agent based
models in [yalla](https://github.com/germannp/yalla).

## Prerequisites

`numba` for paralellisation, [pyvista](https://github.com/marcomusy/vedo) for visualisation with **.vtk**.

For install all the dependences
```bash
pip install -r requirements.txt
```


To initialize the simulation of the fusion of the cell spheroids
```bash
python fusing_spheres.py
```
## Visualization
For a better visualization, its recommended the use of the [ParaView](https://www.paraview.org/) program of the images in the **data** folder. The files are in the **.vtk** format.

#### Initial Conditions
![initial](/markdown/Init.png)
#### Final Conditions
![final](/markdown/Final.png)