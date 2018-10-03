# readCensusExcel.py
# This program will read Census data from an excel spreadsheet
# and get useful data from it

import openpyxl
# import openpyxl.utils
import pprint


def open_wb():
    ''' This function will attempt to open an excel workbook and return it as a workbook object.
        Returns --- OpenPyXl workbook object
    '''
    try:
        wb = openpyxl.load_workbook('censuspopdata.xlsx')
    except:
        print('Unable to open workbook')

    return wb


def get_row_data(sheet):
    ''' This function will take a sheet object, read row data, and save it in a dict.

        Arguments:
        sheet -- OpenPyXl sheet object

        Returns:
        county_data -- a dictionary that stores interesting information
    '''
    county_data = {}

    print('Reading rows...')
    for row in range(2, sheet.max_row + 1):  # we need +1 to include last row
        state = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        population = sheet['D' + str(row)].value

        # Make sure the state key exists, if not create it
        county_data.setdefault(state, {})

        # Make sure county exists for each state, if not create it
        county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

        county_data[state][county]['tracts'] += 1
        county_data[state][county]['pop'] += int(population)

    return county_data


def write_data(data):
    ''' This function will write the data to a file in a python format using pprint module.

        Arguments:
        data -- dictionary containing the data to be written to the file
    '''

    print("Writing data to file...")

    with open('census2010_data.py', 'w') as f:
        f.write(f"all_data = {pprint.pformat(data)}")


def main():
    ''' The main function of the program '''

    print('Opening the workbook...')
    wb = open_wb()

    sheet = wb.active   # gets the active sheet
    data = get_row_data(sheet)

    write_data(data)

    wb.close()


if __name__ == '__main__':
    main()
