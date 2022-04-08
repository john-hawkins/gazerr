import pandas as pd
import numpy as np
import math

def calculate_interval(df, measure, session, top_l_x, top_l_y, bot_r_x, bot_r_y):
    """
    Calculate error bounds on a gaze duration measurement.
    Params
    * df: A dataframe of eye tracking calibration data
    * measure: A gaze duration measurement
    * session: The eye tracking session length
    * top_l_x, top_l_y, bot_r_x, bot_r_y : Top left and bottom right coordinates of target.
    
    Returns: A series of probabilistic error bounds
    """

    if df.columns != ['target_x','target_y','gaze_x','gaze_y']:
        msg = 'Calibration data must consist of columns: target_x, target_y, gaze_x, gaze_y'
        raise Exception('InvalidRequest', msg)

    if measure > session:
        raise Exception('InvalidRequest', 'Measured duration cannot be longer than session')

    # Force measure and session to be rounded integers
    measure = round(float(measure))
    session = round(float(session))

    N = 2000
    D = math.floor(session / 10)
    G = math.floor(measure / 10)
    P = P = np.ndarray([D+1,D+1])

    max_X, max_y = extract_screen_limits(df, bot_r_x, bot_r_y)

    def euclidean(point, ref):
        dist = [(a - b)**2 for a, b in zip(point, ref)]
        dist = math.sqrt(sum(dist))
        return dist

    df['err_x'] = df['gaze_x'] - df['target_x']
    df['err_y'] = df['gaze_y'] - df['target_y']

    df['ref'] = df.apply(lambda x: (x['target_x'],x['target_y']), axis=1)

    x_err = df.groupby('ref')['err_x'].apply(list).reset_index()
    y_err = df.groupby('ref')['err_y'].apply(list).reset_index()

    noise = x_err.copy()
    noise['err_y'] = y_err['err_y']
    def apply_measurement_noise(point):
       """ Use the calibration data to add noise to the path point """
       


    for n in range(0,N):
        in_path = get_path(G, top_l_x, top_l_y, bot_r_x, bot_r_y)
        out_path = get_path(D-G, 0, 0, max_X, max_y, top_l_x, top_l_y, bot_r_x, bot_r_y)
        path = in_path + out_path
        measured_path = [apply_measurement_noise(point) for point in path] 



    result = pd.DataFrame({"Level":[95,90,80], "Lower":[100,140,180], "Upper":[340,390,450]})
    return result

###########################################################
def extract_screen_limits(df, bot_r_x, bot_r_y):
    """
    Take the calibration data and determine the maximum screen size 
    target_x,target_y,gaze_x,gaze_y
    """
    max_X = df['target_x'].max()
    if max_X < bot_r_x:
        max_X = bot_r_x
    max_Y = df['target_y'].max()
    if max_Y < bot_r_y:
        max_Y = bot_r_y
    return max_X,max_Y

###########################################################
def get_path(n, l_x, l_y, r_x, r_y, exc_l_x=-1,exc_l_y=-1,exc_r_x=-1,exc_r_y=-1):
    """
    Get a path of points of length n
    Within the specified bounds.
    Optional parameters to define a space of exclusion
    """
    result = []
    for i in range(0,n):
        valid = False
        while not valid:
            temp_x = random.randrange(l_x, r_x) 
            temp_y = random.randrange(l_y, r_y) 
            if not point_inside(temp_x, temp_y, exc_l_x, exc_l_y, exc_r_x, exc_r_y):
                valid = True
        result.append( (temp_x, temp_y) )

    return result
 
###########################################################
def point_inside(temp_x, temp_y, exc_l_x, exc_l_y, exc_r_x, exc_r_y):
    if temp_x >= exc_l_x & temp_x <= exc_r_x & temp_y >= exc_l_y & temp_y <= exc_r_y:
        return True
    else:
        return False








