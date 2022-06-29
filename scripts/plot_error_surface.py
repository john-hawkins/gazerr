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

def generate_2d_surface_plot(dim1, dim2, dim3, colone, coltwo, value):
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
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

colone="Fixation Error"
coltwo="Measured Duration" 
value="Duration Error"

myplot = generate_2d_surface_plot(dim1, dim2, dim3, colone, coltwo, value)

myplot.savefig("results/Error_surface.png")

