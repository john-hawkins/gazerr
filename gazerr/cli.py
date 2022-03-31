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

    parser.add_argument('ad_position',
                       metavar='ad_position',
                       type=str,
                       help='Position of the ad in the viewport. Values: top | mid | bot')
    parser.add_argument('output',
                       metavar='output',
                       type=str,
                       help='Path to output file location.')
 
    parser.add_argument('-f', '--force', action="store_true", help="Force the output overwrite.")
    args = parser.parse_args()
    data = args.calibration_data
    measure = args.measurement
    session = args.session_length
    position = args.ad_position
    output = args.output

    if not os.path.isfile(data):
        print(" ERROR")
        print(" The input file '%s' does not exist" % data)
        sys.exit()

    if os.path.isfile(output) and not args.force:
        print(" ERROR")
        print(" The output file '%s' already exists."% output)
        print("    Use -f [--force] to force an overwrite over the file")

    df = load_calibration_data(data)
    result = run_simulation(df, measure, session, position)
    result.to_csv(output, index=False, header=True)

##########################################################################################
if __name__ == '__main__':
    main()


