"""
Application for converting .csv file to .json file
"""

import csv, json, os


def read_csv(file):
    # Read .csv file and store it into dictionary
    data = {}

    with open(file, "r") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            _id = csvRow["id"]
            data[_id] = csvRow
    return data
    # try:
    #     if csvFile
    # csvFilePath = "pipeline_input_user_export.csv"
    # jsonFilePath = "pipeline_input_user_export.json"


def write_json(data, file):
    #Write data into a .json file
    with open(file, "w") as jsonFile:
        jsonFile.write(json.dumps(data))

# Testing
# csvFilePath = "pipeline_input_user_export.csv"
# jsonFilePath = "D:\dataScience\Corteva\pipeline_input_user_export.json"
#
# rc = read_csv(csvFilePath)
# wj = write_json(rc, jsonFilePath)

if __name__ == '__main__':
    csvFilePath = input("Please enter .csv file: ")
    jsonFilePath = os.path.splitext(csvFilePath)[0]+".json"
    write_json(read_csv(csvFilePath), jsonFilePath)
