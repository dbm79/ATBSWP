#! python3
# regex-search.py - searches files in a folder for matches to a user provided regex

import sys, re, os


def print_usage():
    """ This function will print the usage information if too few command-line arguments are given """
    print(
        f"""
Usage:
python regex-search <directory with text files to search>
    """
    )


def check_folder(folder):
    """ This function will check the folder relative to current path verify it exists
        Param1: folder name to verify
        Returns: folder name
    """

    while True:
        if os.path.exists(folder) and os.path.isdir(folder):
            return folder
        else:
            print(f"\n{folder} does not exist or is not a folder\n")
            folder = input(
                f"Please enter the folder to search relative to {os.getcwd()}: "
            )


def get_regex():
    """ This function will ask the user for a regex and create a compiled regex object
        Returns: Compiled regex object
    """
    pattern = input("\n\nPlease enter a regex pattern to search for: ")
    regex = re.compile(pattern)

    return regex


def get_files(folder):
    """ This function/generator will get all the files names in the folder and yeild one file at a time
        it will exit if no exit if no files found.
        Param1: folder to get files from
        Yields: file name
    """
    files = os.listdir(folder)

    if len(files) > 0:
        for file in files:
            yield file
    else:
        print(f"No files found in folder: {folder}")
        sys.exit(0)


def open_files(folder):
    """ This function is a generator that will open a file for reading and return a file object
        Param1: string for the folder that contains the files
        Yields: a file object in read mode
    """

    for file in get_files(folder):
        yield open(os.path.join(folder, file), "r")


def get_line(file):
    """ This function will read all of the file's lines return a single lime with its index + 1.
        Param1: A file object
        Yields: Enumerated index+1 and the line itself
    """

    contents = file.readlines()

    for line_num, line in enumerate(contents, 1):
        yield line_num, line


def find_matches(folder, regex):
    """ This function will changes to the folder, open the files one-by-one
        get their contents, try and find regex matches
        
        Param1: folder that contns the files to search
        Param2: compiled regex object
    """

    for file in open_files(folder):
        matches = {}

        for line_num, line in get_line(file):
            match = regex.search(line)

            if match:
                matches[line_num] = line

        if len(matches) > 0:
            print(f"\n{len(matches)} match(s) found in file: {file.name}")
            print(matches)
        else:
            print(f"No match found in file {file.name}")


def main(arguments):
    """ This is the main part of the program
        Param1: list of argumets from sys.argv
    """

    if len(arguments) < 2:  # Make sure user entered folder as runtime argument
        print_usage()
    else:

        folder = check_folder(arguments[1])

        regex = get_regex()

        find_matches(folder, regex)


if __name__ == "__main__":
    main(sys.argv)
