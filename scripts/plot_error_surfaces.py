import pandas as pd
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mpl

file_prefix = "results/MREC_MAE_"
filename = "/expected_values.csv"

errors = [20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]

D = 21
dim1 = []
dim2 = []
dim3 = []

v2_dim1 = []
v2_dim2 = []
v2_dim3 = []

def generate_2d_surface_plot(ax, dim1, dim2, dim3, colone, coltwo, value):
    ax.plot_trisurf(dim1, dim2, dim3, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_xlabel(colone)
    ax.set_ylabel(coltwo)
    ax.set_zlabel(value)
    return plt

for i,err in enumerate(errors):
    file = file_prefix + str(err) + filename
    df = pd.read_csv(file)
    df['error'] = abs(df['Measured']-df['Expected'])
    for m,e in zip(df['Measured'], df['error']):
       dim1.append(err)
       dim2.append(m)
       dim3.append(e)
       if m!=e:
          v2_dim1.append(err)
          v2_dim2.append(m)
          v2_dim3.append(e)

colone="Fixation Error"
coltwo="Measured Duration" 
value="Duration Error"

# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))

# =============
# First subplot
# =============
# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')

# plot a 3D surface like in the example mplot3d/surface3d_demo

#surf = ax.plot_surface(dim1, dim2, dim3, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.plot_trisurf(dim1, dim2, dim3, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_xlabel(colone)
ax.set_ylabel(coltwo)
ax.set_zlabel("")
#fig.colorbar(surf, shrink=0.5, aspect=10)

# ==============
# Second subplot
# ==============
# set up the axes for the second plot
ax = fig.add_subplot(1, 2, 2, projection='3d')

# plot a 3D wireframe like in the example mplot3d/wire3d_demo
#surf = ax.plot_surface(v2_dim1, v2_dim2, v2_dim3, rstride=1, cstride=1, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)
ax.plot_trisurf(v2_dim1, v2_dim2, v2_dim3, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_xlabel(colone)
ax.set_ylabel(coltwo)
ax.set_zlabel(value)

plt.show()


#plt.savefig("results/Error_surfaces.png")

