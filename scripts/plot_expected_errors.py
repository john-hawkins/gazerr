import pandas as pd
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt

file_prefix = "results/MREC_MErr_"
file_prefix2 = "results/MREC_MErr_Biased_"
file_prefix2 = "results/MREC_MErr_Biased_"
file_prefix3 = "results/MREC_MErr_Biased_Precise_"
filename = "/expected_values.csv"

errors = [20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]
gaze_err_uni = []
gaze_err_exp = []
gaze_err2_uni = []
gaze_err2_exp = []
gaze_err3_uni = []
gaze_err3_exp = []

# This creates the weighting for measurements
x = expon.rvs(scale=30, size=10000)
vals = plt.hist(x, density=False, edgecolor='black', bins=21)
vallist = vals[0].tolist() 
dist_exp = [x / sum(vallist) for x in vallist]
dist_uni = [1/len(vallist) for x in vallist]

for err in errors:
    file = file_prefix + str(err) + filename
    file2 = file_prefix2 + str(err) + filename
    file3 = file_prefix3 + str(err) + filename
    df = pd.read_csv(file)
    df2 = pd.read_csv(file2)
    df3 = pd.read_csv(file3)
    df['error'] = abs(df['Measured']-df['Expected'])
    df2['error'] = abs(df2['Measured']-df2['Expected'])
    df3['error'] = abs(df3['Measured']-df3['Expected'])
    df['uni'] = dist_uni
    df['exp'] = dist_exp
    df['err_uni'] = df['error']*df['uni'] 
    df['err_exp'] = df['error']*df['exp'] 
    gaze_err_uni.append(df['err_uni'].sum())
    gaze_err_exp.append(df['err_exp'].sum()) 
    df2['uni'] = dist_uni
    df2['exp'] = dist_exp
    df2['err_uni'] = df2['error']*df2['uni'] 
    df2['err_exp'] = df2['error']*df2['exp'] 
    gaze_err2_uni.append(df2['err_uni'].sum())
    gaze_err2_exp.append(df2['err_exp'].sum()) 
    df3['uni'] = dist_uni
    df3['exp'] = dist_exp
    df3['err_uni'] = df3['error']*df3['uni'] 
    df3['err_exp'] = df3['error']*df3['exp'] 
    gaze_err3_uni.append(df3['err_uni'].sum())
    gaze_err3_exp.append(df3['err_exp'].sum()) 

fig = plt.figure(figsize=(22,8))
#fig = plt.figure(figsize=plt.figaspect(0.5))

# =============
# First subplot
# =============
# set up the axes for the first plot
ax = fig.add_subplot(1, 3, 1)
ax.set_title('A) Expected Error - Gaze Fixation Vs Duration')
ax.plot(errors, gaze_err_uni, c='firebrick', label="Uniform Measurement Distribution")
ax.plot(errors, gaze_err_exp, c='salmon', linestyle='dashed', label="Exponential Measurement Distribution")
ax.set_xlabel('Gaze Fixation μ Error (px)', fontsize=12)
ax.set_ylabel('Gaze Duration μ Error (ms)', fontsize=12)
ax.set_xlim([0, 175])
ax.set_ylim([0, 500])
ax.legend( prop={'size': 10} )

ax = fig.add_subplot(1, 3, 2)
ax.set_title('B) Expected Error - Biased Gaze Fixation Vs Duration')
ax.plot(errors, gaze_err2_uni, c='seagreen', label="Uniform Measurement Distribution")
ax.plot(errors, gaze_err2_exp, c='lightseagreen', linestyle='dashed', label="Exponential Measurement Distribution")
ax.set_xlabel('Gaze Fixation μ Error (px)', fontsize=12)
ax.set_ylabel('Gaze Duration μ Error (ms)', fontsize=12)
ax.set_xlim([0, 175])
ax.set_ylim([0, 500])
ax.legend( prop={'size': 10} )

ax = fig.add_subplot(1, 3, 3)
ax.set_title('C) Expected Error - Biased Precise Gaze Fixation Vs Duration')
ax.plot(errors, gaze_err3_uni, c='darkorchid', label="Uniform Measurement Distribution")
ax.plot(errors, gaze_err3_exp, c='orchid', linestyle='dashed', label="Exponential Measurement Distribution")
ax.set_xlabel('Gaze Fixation μ Error (px)', fontsize=12)
ax.set_ylabel('Gaze Duration μ Error (ms)', fontsize=12)
ax.set_xlim([0, 175])
ax.set_ylim([0, 500])
ax.legend( prop={'size': 10} )

plt.savefig("results/Fixation_vs_duration_error.png")

