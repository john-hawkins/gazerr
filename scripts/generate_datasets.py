import math
import random
import pandas as pd

header = ["target_x","target_y","gaze_x","gaze_y"]

maes = [20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]

# We roughly approximate an iPhone 7 
# Which has a viewport dimensions of 375px × 667
#  (number of software pixels (CSS pixels) present on a screen) 
device_width = 375
device_height = 667

N = 1500

def add_noise(x,y,maerr, bias=False):
    factor = 1.85
    part = math.sqrt(math.pow(maerr,2)/2)
    x_err = random.uniform(-part*factor,part*factor)
    y_err = random.uniform(-part*factor,part*factor)
    if bias:
        x_err = -abs(x_err)
        y_err = -abs(y_err)
    return x+x_err,y+y_err

def euclidean(row):
    return math.sqrt(
       math.pow(row["target_x"] - row["gaze_x"], 2) +
       math.pow(row["target_y"] - row["gaze_y"], 2)
    )

for mae in maes:
    results = pd.DataFrame(columns=header)
    results2 = pd.DataFrame(columns=header)
    filename = "data/validation_%s_MAE.csv"%str(mae)
    filename2 = "data/validation_%s_MAE_Biased.csv"%str(mae)
    for n in range(N):
        my_x = random.randrange(0, device_width, 20)
        my_y = random.randrange(0, device_height, 20)
        gaze_x, gaze_y = add_noise(my_x,my_y,mae)
        results = results.append({
              "target_x":my_x,
              "target_y":my_y,
              "gaze_x":gaze_x,
              "gaze_y":gaze_y
           }, ignore_index=True
        )
        gaze_x, gaze_y = add_noise(my_x,my_y,mae,bias=True)
        results2 = results2.append({
              "target_x":my_x,
              "target_y":my_y,
              "gaze_x":gaze_x,
              "gaze_y":gaze_y
           }, ignore_index=True
        )
    results.to_csv(filename, index=False,header=True)
    results2.to_csv(filename2, index=False,header=True)
    results2['error'] = results.apply(euclidean, axis=1)
    print("Expected MAE: ", mae)
    print("Simulated MAE: ", results2['error'].mean())



