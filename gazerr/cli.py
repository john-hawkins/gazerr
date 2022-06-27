import pandas as pd
import argparse
import sys
import os

from .estimate import calculate_interval

####################################################################################
def load_calibration_data(input_path):
    df = pd.read_csv(input_path, low_memory=False)
    return df

####################################################################################
def run_simulation(df, measure, session, top_left, bot_right, posterior):
    top = top_left.split(",")
    bot = bot_right.split(",")
    if len(top) != 2:
        print("TOP LEFT COORDINATES MUST BE A COMMA SEPARATED PAIR OF INTEGERS")
        exit(1)
    if len(bot) != 2:
        print("BOTTOM RIGHT COORDINATES MUST BE A COMMA SEPARATED PAIR OF INTEGERS")
        exit(1)
    try:
        tlx = int(top[0]) 
        tly = int(top[1])
    except:
        print("TOP LEFT COORDINATES MUST BE A COMMA SEPARATED PAIR OF INTEGERS")
        exit(1)
    try:
        brx = int(bot[0]) 
        bry = int(bot[1])
    except:
        print("BOTTOM RIGHT COORDINATES MUST BE A COMMA SEPARATED PAIR OF INTEGERS")
        exit(1)

    results = calculate_interval(df, measure, session, tlx, tly, brx, bry)
    return results

####################################################################################
def main():
    desc = 'Estimate Gaze Duration Error Distribution from Eye Tracking Data'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('calibration_data',
                       metavar='calibration_data',
                       type=str,
                       help='Path to the model calibration data contains targets and gaze coords - Requires columns [target_x, target_y, gaze_x, gaze_y]')

    parser.add_argument('measurement',
                       metavar='measurement',
                       type=float,
                       help='Measured gaze duration (in milliseconds) [for which we want error bounds].')

    parser.add_argument('session_length',
                       metavar='session_length',
                       type=float,
                       help='Length of total viewing session (in milliseconds) [Max in principle gaze duration]')

    parser.add_argument('target_top_left',
                       metavar='target_top_left',
                       type=str,
                       help='X,Y Position for top left of target bounding box.')

    parser.add_argument('target_bottom_right',
                       metavar='target_bottom_right',
                       type=str,
                       help='X,Y Position for bottom right of target bounding box.')

    parser.add_argument('posterior_file',
                       metavar='posterior_file',
                       type=str,
                       help='Path to write out the posterior distribution.')

    args = parser.parse_args()
    data = args.calibration_data
    measure = args.measurement
    session = args.session_length
    top_left = args.target_top_left
    bottom_right = args.target_bottom_right
    posterior = args.posterior_file

    if not os.path.isfile(data):
        print(" ERROR")
        print(" The input file '%s' does not exist" % data)
        sys.exit()

    df = load_calibration_data(data)
    result = run_simulation(df, measure, session, top_left, bottom_right, posterior)
    print(result)

##########################################################################################
if __name__ == '__main__':
    main()


