import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

df = pd.read_csv("data/eye_tracking_gaze_log.csv")

df = df[df['eye_tracking_state']=='success']

def euclidean_distance(row):
    xdiff = row['target_x'] - row['gaze_x']
    ydiff = row['target_y'] - row['gaze_y']
    return math.sqrt( math.pow(xdiff,2) + math.pow(ydiff,2) )

df['ERR'] = df.apply(euclidean_distance,axis=1)

group_cols = ['user_ext', 'event_type', 'target_state', 'event_counter']

grpd = df.groupby(group_cols)

rez = pd.DataFrame(columns=['user_ext', 'event_type', 'target_state', 'event_counter','ERR'])

for _cols, _df in grpd:
    srted = _df.sort_values(by='timestamp', axis=0, ascending=True).reset_index()
    error = srted.loc[len(srted)-3,:]['ERR']
    rez = rez.append(
        {
            'user_ext':_cols[0], 
            'event_type':_cols[1], 
            'target_state':_cols[2], 
            'event_counter':_cols[3],
            'error':error
        },
        ignore_index=True
    )


print(rez.groupby(['event_type','target_state'])['error'].mean())
# event_type   target_state
# calibration  calibrating     347.418435
#              validating       80.452925
# validation   validating       76.395421

print(rez.groupby(['event_type','target_state'])['error'].median())
# event_type   target_state
# calibration  calibrating     349.082198
#             validating       69.956001
# validation   validating       63.249788

##################################################################
 
temp = df[df['target_destroyed']==True ]

grpd2 = temp.groupby(group_cols)
rez2 = pd.DataFrame(columns=['user_ext', 'event_type', 'target_state', 'event_counter'])
for _cols, _df in grpd2:
    srted = _df.sort_values(by='timestamp', axis=0, ascending=True).reset_index()
    error = srted.loc[0,:]['ERR']
    rez2 = rez2.append(
        {
            'user_ext':_cols[0],
            'event_type':_cols[1],
            'target_state':_cols[2],
            'event_counter':_cols[3],
            'error':error
        },
        ignore_index=True
    )




