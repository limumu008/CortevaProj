import csv, json, os
import argparse
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "pipeline.log", level = logging.DEBUG, format = log_format, filemode = 'w')
logger = logging.getLogger()

def csv_to_json(csvFile, jsonFile):
    '''
    Convert .csv file to .json file
    :param csvFile: .csv file
    :param jsonFile: .json file
    :return: None
    '''

    # Create data as a dictionary for storing the data from csv file
    data = {}
    # Read a csv file
    logger.debug('# Open csv file')
    with open(csvFile, "r") as c:
        csvReader = csv.DictReader(c)
        try:
            for csvRow in csvReader:
                _id = csvRow["id"]
                data[_id] = csvRow
        except csv.Error as e:
            logging.exception('file {}, line {}: {}'.format(csvFile, csvReader.line_num, e))
    #Write data into a .json file
    logger.debug('# Write json file')
    try:
        with open(jsonFile, "w") as j:
            j.write(json.dumps(data, indent="\t"))
        logger.debug("# CSV file is complete converted to JSON file!")
    except Exception as e:
        logging.exception(e)

def main():
    '''
    CLI program defines .csv file as an input and .json file as an output argument.
    It generates the help, useage messages and errors with logging.
    '''
    parser = argparse.ArgumentParser(description="Convert a .csv file to a .json file")
    parser.add_argument('-in', '--csvFile', metavar='', help="CSV input file", type=str, required=True)
    parser.add_argument('-out', '--jsonFile', metavar='', help="JSON output file",  type=str, required=True)
    args = parser.parse_args()
    logger.info("csv_to_json({0}, {1})".format(args.csvFile, args.jsonFile))
    try:
        if os.path.splitext(args.csvFile)[1] != '.csv':
            logger.error('# Input file has to be a csv file! e,g test.csv ')
            raise FileNotFoundError
        if os.path.splitext(args.jsonFile)[1] != '.json':
            logger.error('# Output file has to be a json file! e,g test.json')
            raise FileExistsError
        else:
            csv_to_json(args.csvFile, args.jsonFile)
    except (FileExistsError, FileNotFoundError) as e:
        logging.exception(e)
        raise

if __name__ == '__main__':
    main()