# text_to_spreadsheet.py
# This will read the text if text files and put each line in a row in a column for each file

import openpyxl
import os


def open_workbook():
    ''' This function will attempt to open an excel workbook and return it as a workbook object.
        Returns --- OpenPyXl workbook object
    '''
    try:
        workbook = openpyxl.Workbook()
    except:
        print('Unable to open spreadsheet.')

    return workbook


def get_file_contents(file):
    ''' This function will open a file and read all of the lines and return a list of all the lines in the text.

    Arguments:
    file -- the name of the file to open

    Returns:
    lines -- a list of the lines
    '''

    with open(file, 'r') as f:
        lines = f.readlines()

    return lines


def main():
    ''' This is the main function of the program '''

    files = ['invictus.txt', 'raven.txt']

    wb = open_workbook()
    sheet = wb.active

    for i in range(len(files)):
        contents = get_file_contents(files[i])

        for j in range(len(contents)):
            sheet.cell(row=j + 1, column=i + 1).value = contents[j]

    wb.save('text_to_spreadsheet.xlsx')
    wb.close()


if __name__ == "__main__":
    main()
