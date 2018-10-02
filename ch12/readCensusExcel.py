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

        pprint.pprint(state + ': ' + str(population))


def main():
    ''' The main function of the program '''

    print('Opening the workbook...')
    wb = open_wb()

    sheet = wb.get_active_sheet()
    get_row_data(sheet)

    wb.close()


if __name__ == '__main__':
    main()
