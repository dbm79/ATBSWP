# update_produce.py
# This program will open a spreadsheet and update various produce prices

import openpyxl


def open_workbook():
    ''' This function will attempt to open an excel workbook and return it as a workbook object.
        Returns --- OpenPyXl workbook object
    '''
    try:
        workbook = openpyxl.load_workbook('produceSales.xlsx')
    except:
        print('Unable to open spreadsheet.')

    return workbook


def main():
    ''' This is the main function of the program. '''

    wb = open_workbook()


if __name__ == '__main__':
    main()
