"""
Application for converting .csv file to .json file
"""

import csv, json, sys
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

def main():
    parser = argparse.ArgumentParser(description="Convert a .csv file to a .json file")
    parser.add_argument('-in', '--csvFile', metavar='', help="CSV input file", type=str, required=True)
    parser.add_argument('-out', '--jsonFile', metavar='', help="JSON output file",  type=str, required=True)
    args = parser.parse_args()
    csv_to_json(args.csvFile, args.jsonFile)

if __name__ == '__main__':
    main()