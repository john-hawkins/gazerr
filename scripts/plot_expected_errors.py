import pandas as pd
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt

file_prefix = "results/MREC_MAE_"
filename = "/expected_values.csv"

errors = [20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]
gaze_err_uni = []
gaze_err_exp = []

# This creates the weighting for measurements
x = expon.rvs(scale=30, size=10000)
vals = plt.hist(x, density=False, edgecolor='black', bins=21)
vallist = vals[0].tolist() 
dist_exp = [x / sum(vallist) for x in vallist]
dist_uni = [1/len(vallist) for x in vallist]

for err in errors:
    file = file_prefix + str(err) + filename
    df = pd.read_csv(file)
    df['error'] = abs(df['Measured']-df['Expected'])
    df['uni'] = dist_uni
    df['exp'] = dist_exp
    df['err_uni'] = df['error']*df['uni'] 
    df['err_exp'] = df['error']*df['exp'] 
    gaze_err_uni.append(df['err_uni'].sum())
    gaze_err_exp.append(df['err_exp'].sum()) 

fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot()

ax.set_title('Fixation Vs Duration Expected Error')
ax.plot(errors, gaze_err_uni, c='darkorange', label="Uniform Measurement Distribution")
ax.plot(errors, gaze_err_exp, c='teal', label="Exponential Measurement Distribution")
ax.set_xlabel('Gaze Fixation μ Error (px)', fontsize=15)
ax.set_ylabel('Gaze Duration μ Error (ms)', fontsize=15)
ax.set_xlim([0, 175])
ax.legend( prop={'size': 15} )

plt.savefig("results/Fixation_vs_duration_error.png")

