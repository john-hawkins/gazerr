import pandas as pd
import argparse
import sys
import os

####################################################################################
def load_calibration_data(input_path):
    df = pd.read_csv(input_path, low_memory=False)
    return df

####################################################################################
def run_simulation(df):
    results = pd.DataFrame()
    locations = ["Banner Top", "Banner Bottom", "Banner Centre"]
    for loc in locations:
       record = {}
       record['Location'] = loc
       record['Error'] = 20
       results.append(record, ignore_index=True)
    return results

####################################################################################
def main():
    desc = 'Estimate Gaze Duration Error Distribution from Eye Tracking Data'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('calibration_data',
                       metavar='calibration_data',
                       type=str,
                       help='Path to the model calibration data contains targets and gaze coords')

    parser.add_argument('measurement',
                       metavar='measurement',
                       type=float,
                       help='Measured gaze duration.')

    parser.add_argument('session_length',
                       metavar='session_length',
                       type=float,
                       help='Measured gaze duration.')

    parser.add_argument('ad_position',
                       metavar='ad_position',
                       type=str,
                       help='Position of the ad in the viewport: top | mid | bottom')
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
    result = run_simulation(df)
    result.to_csv(output, index=False, header=True)

#############################################################
def print_usage(args):
    """ Command line application usage instructions. """
    print("USAGE ")
    print(args[0], " <VALIDATION DATASET> <MEASUREMENT> <SESSION LENGTH> <AD POSITION> <OUTPUT>")
    print(" <VALIDATION DATASET> - Supported file types: csv")
    print(" <MEASUREMENT> - Measured gaze duration (seconds)")
    print(" <SESSION LENGTH> - Length of the media viewing session (seconds)")
    print(" <AD POSITION> - Position in the viewport of the ad unit (top|mid|bottom)")
    print(" <OUTPUT> - Output path to write the results file")
    print("")


##########################################################################################
if __name__ == '__main__':
    main()


