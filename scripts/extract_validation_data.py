import pandas as pd
import numpy as np
import math

df = pd.read_csv("data/eye_tracking_gaze_log.csv")
df = df[df['eye_tracking_state']=='success']
df = df[ df['target_state']=='validating' ]

# Group by the following so we get a single stream of events for each validation target
group_cols = ['user_ext', 'event_type', 'target_state', 'event_counter']

grpd = df.groupby(group_cols)

rez = pd.DataFrame(columns=['target_x', 'target_y', 'gaze_x','gaze_y'])

for _cols, _df in grpd:
    srted = _df.sort_values(by='timestamp', axis=0, ascending=True).reset_index()
    index_of_destroyed = -1
    found = False
    pos = -1
    while not found:
        if srted.loc[len(srted)+pos,:]['target_destroyed']==True:
            index_of_destroyed = pos
            found = True
        pos = pos - 1
        if len(srted)+pos < 0:
            break
    if found:
        for i in range(0,5):
            temp = srted.loc[len(srted)+pos-i,:]
            rez = rez.append(
               {
                'target_x': temp['target_x'], 
                'target_y': temp['target_y'],
                'gaze_x': temp['gaze_x'],
                'gaze_y': temp['gaze_y']
               },
               ignore_index=True
            )

rez.to_csv("data/validation_data.csv", header=True, index=False)
 

