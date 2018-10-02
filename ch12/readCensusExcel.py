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

    pprint.pprint(county_data)


def main():
    ''' The main function of the program '''

    print('Opening the workbook...')
    wb = open_wb()

    sheet = wb.active   # gets the active sheet
    get_row_data(sheet)

    wb.close()


if __name__ == '__main__':
    main()
