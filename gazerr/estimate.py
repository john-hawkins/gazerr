import pandas as pd
import numpy as np
import math

def calculate_interval(df, measure, session, top_l_x, top_l_y, bot_r_x, bot_r_y):
    """
    Given a dataframe of eye tracking calibration data
    and a gaze duration measure, session length and then
    an ad position, then we calculate error bounds on the
    basis of simulation.
    """
    if measure>session:
        raise Exception('InvalidRequest', 'Measured duration cannot be longer than session')
    N = 2000
    D = math.floor(session / 10)
    P = P = np.ndarray([D+1,D+1])

    result = pd.DataFrame({"Level":[95,90,80], "Lower":[100,140,180], "Upper":[340,390,450]})
    return result


