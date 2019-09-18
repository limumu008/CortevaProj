"""
Application for converting .csv file to .json file
"""

import csv, json, os, sys
import argparse

def csv_to_json(csvFile, jsonFile):
    # Read .csv file and store it into dictionary
    data = {}
    with open(csvFile, "r") as c:
        csvReader = csv.DictReader(c)
        try:
            for csvRow in csvReader:
                _id = csvRow["id"]
                data[_id] = csvRow
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(csvFile, csvReader.line_num, e))
    #Write data into a .json file
    try:
        with open(jsonFile, "w") as j:
            j.write(json.dumps(data, indent="\t"))
        print("CSV file is complete converted!")
    except Exception as e:
        print("Error occured:", e)
# Testing
# csvFilePath = "pipeline_input_user_export.csv"
# jsonFilePath = "D:\dataScience\Corteva\pipeline_input_user_export.json"
#
# rc = read_csv(csvFilePath)
# wj = write_json(rc, jsonFilePath)
def main():
    parser = argparse.ArgumentParser(description="Convert a .csv file to a .json file")
    parser.add_argument('-in', '--input', help="CSV input file", type=str)
    parser.add_argument('-out', '--output', help="JSON output file",  type=str)
    #parser.add_argument()
    #parser.set_defaults(func=csv_to_json)
    args = parser.parse_args()
    csv_to_json(args.input, args.output)
    # csvFilePath = input("Please enter .csv file: ")
    # jsonFilePath = os.path.splitext(csvFilePath)[0] + ".json"
    # dt = read_csv(csvFilePath)
    # write_json(dt, jsonFilePath)

if __name__ == '__main__':
    main()