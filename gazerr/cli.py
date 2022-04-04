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
def run_simulation(df, measure, session, position):
    results = calculate_interval(df, measure, session, position)
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
                       help='Measured gaze duration [for which we want error bounds].')

    parser.add_argument('session_length',
                       metavar='session_length',
                       type=float,
                       help='Length of total viewing session [Max in principle gaze duration]')

    parser.add_argument('target_top_left',
                       metavar='target_top_left',
                       type=str,
                       help='X,Y Position for top left of target bounding box.')

    parser.add_argument('target_bottom_right',
                       metavar='target_bottom_right',
                       type=str,
                       help='X,Y Position for bottom right of target bounding box.')

    args = parser.parse_args()
    data = args.calibration_data
    measure = args.measurement
    session = args.session_length
    top_left = args.target_top_left
    bottom_right = args.target_bottom_right

    if not os.path.isfile(data):
        print(" ERROR")
        print(" The input file '%s' does not exist" % data)
        sys.exit()

    df = load_calibration_data(data)
    result = run_simulation(df, measure, session, top_left, bottom_right)
    print(result)

##########################################################################################
if __name__ == '__main__':
    main()


