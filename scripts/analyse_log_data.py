import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

df = pd.read_csv("data/eye_tracking_gaze_log.csv")
print(f"Total records {len(df)}")

df = df[df['eye_tracking_state']=='success']
print(f"Successful records {len(df)}")
print(f"From {min(df['timestamp'])} to {max(df['timestamp'])} ")

print(f"Calibration Records {len(df[df['event_type']=='calibration'])}")
print(f"Validation Records {len(df[df['event_type']=='validation'])}")

print("Target Numbers for Calibration")
print(df[df['event_type']=='calibration']['target_number'].value_counts())
print("Target Numbers for Validation")
print(df[df['event_type']=='validation']['target_number'].value_counts())

def euclidean_distance(row):
    xdiff = row['target_x'] - row['gaze_x']
    ydiff = row['target_y'] - row['gaze_y']
    return math.sqrt( math.pow(xdiff,2) + math.pow(ydiff,2) )

df['ERR'] = df.apply(euclidean_distance,axis=1)

# Basics
print("Total mean:",df['ERR'].mean())
print("Total median:",df['ERR'].median())
print("calibration mean", df[df['event_type']=="calibration"]['ERR'].mean())
print("calibration median", df[df['event_type']=="calibration"]['ERR'].median())
print("validation mean", df[df['event_type']=="validation"]['ERR'].mean())
print("validation median", df[df['event_type']=="validation"]['ERR'].median())

dataset = df[df['event_type']=="calibration"]['target_number'].value_counts().reset_index()
plt.scatter(dataset['index'], dataset['target_number'])
plt.title("Record count by target_number for calibration data")
plt.xlabel("target_number")
plt.ylabel("count")
plt.savefig("results/records_by_target_number.png")


df['ERR'].hist(bins=100)
plt.title("Error Distribution")
plt.savefig("results/Error_Distribution.png",format='png', dpi=100, bbox_inches='tight')

tech = ['eye_tracking_calibration_mode','device_model', 'os', 'os_version']
groups = [ 'study_id', 'user_id', 'user_ext', 'session_id']

# Create subplots 
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), dpi=100)
fig.subplots_adjust(hspace=0.5)
fig.suptitle('Distribution of Gaze Fixation Mean Error by Grouping')

for ax, grp in zip(axes.flatten(), groups):
    temp = df.groupby(grp)['ERR'].mean().reset_index()
    temp['ERR'].hist(bins=50, ax=ax)
    ax.set_title(grp)

plt.savefig("results/Grouped_Mean_Error_Distribution.png", format='png', dpi=100, bbox_inches='tight')

# Create subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), dpi=100)
fig.subplots_adjust(hspace=0.5)
fig.suptitle('Distribution of Gaze Fixation Max Error by Grouping')

for ax, grp in zip(axes.flatten(), groups):
    temp = df.groupby(grp)['ERR'].max().reset_index()
    temp['ERR'].hist(bins=50, ax=ax)
    ax.set_title(grp)

plt.savefig("results/Grouped_Max_Error_Distribution.png", format='png', dpi=100, bbox_inches='tight')

###################

calib_targets = df[df['event_type']=="calibration"].groupby('target_number').agg({'user_id':["count","nunique"],"ERR":["min","mean","max"]}).reset_index()

calib_targets.to_csv("results/calibration_target_numbers_stats.csv")

#######################################
# Looking at position on the screen


for dev in df['device_model'].unique():
    temp = df[df['device_model']==dev].copy()
    xmax = temp['target_x'].max() 
    ymax = temp['target_y'].max() 
    xmid = xmax/2
    yf = ymax/3
    ys = 2*ymax/3
    def get_position(row):
        if row['target_y'] < yf:
            if row['target_x'] < xmid:
               return 0
            else:
               return 1
        elif row['target_y'] < ys:
            if row['target_x'] < xmid:
               return 2
            else:
               return 3
        else:
            if row['target_x'] < xmid:
               return 4
            else:
               return 5
    temp['gridPos'] = temp.apply(get_position, axis=1)    
    # Create subplots
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 8), dpi=100)
    fig.subplots_adjust(hspace=0.5)
    fig.suptitle(f"Gaze Fixation Error by Screen Position for {dev}")
    grid_positions = [0,1,2,3,4,5]
    for ax, grp in zip(axes.flatten(), grid_positions):
        temp2 = temp[temp['gridPos']==grp]
        temp2['ERR'].hist(bins=50, ax=ax)
        ax.set_xlim(0, 1000)
    plt.savefig(f"results/{dev}_Error_Distribution.png", format='png', dpi=100, bbox_inches='tight')



