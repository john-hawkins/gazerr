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
    parser = argparse.ArgumentParser(description='Run Error Estimation Experiment.')

    parser.add_argument('input',
                       metavar='input',
                       type=str,
                       help='Path to the model calibration data.')

    parser.add_argument('output',
                       metavar='output',
                       type=str,
                       help='Path to output file location.')

    parser.add_argument('-f', '--force', action="store_true", help="Force the output to overwrite existing files")

    # Execute the parse_args() method
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    if not os.path.isfile(input_path):
        print(" ERROR")
        print(" The input file '%s' does not exist" % input_path)
        sys.exit()

    if os.path.isfile(output_path) and not args.force:
        print(" ERROR")
        print(" The output file '%s' already exists."% output_path)
        print("    Use -f [--force] to force an overwrite over the file")
        sys.exit()

    df = load_calibration_data(input_path)

    result = run_simulation(df)

    result.to_csv(output_path, index=False, header=True)



####################################################################################
if __name__ == '__main__':
    main()


