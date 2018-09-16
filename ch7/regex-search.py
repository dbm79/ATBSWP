#! python3
# regex-search.py - searches files in a folder for matches to a user provided regex

import sys, re, os


def print_usage():
    """ This function will print the usage information if too few command-line arguments are given """
    print(
        f"""
Usage:
python regex-search <directroy with textfiles to search>
    """
    )


def get_folder(folder):
    """ This function will get the folder-name relative to current path from the user and verify it exists
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


def get_files(folder):
    """ This function will get all the files names in the folder
        Param1: folder to get files from
        Returns: list of file names
    """
    files = os.listdir(folder)
    if len(files) > 0:
        return files
    else:
        print(f"No files found in folder")
        sys.exit(0)


def get_regex():
    """ This function will ask the user for a regex and create a compiled regex object
        Returns: Compiled regex object
    """
    pattern = input("\n\nPlease enter a regex pattern to search for: ")
    regex = re.compile(pattern)
    # print(regex.pattern)
    return regex


def find_matches(folder, files, regex):
    """ This function will changes to the folder, open the files one-by-one
        get their contents, try and find regex matches
        
        Param1: folder that contns the files to search
        Param2: list of files to search
        Param3: compiled regex object
    """

    for file in files:
        matches = {}

        with open(
            os.path.join(folder, file), "r"
        ) as f:  # os.path.join used to join the folder and file name
            contents = f.readlines()

            for line_num, line in enumerate(contents, 1):
                match = regex.search(line)

                if match:
                    matches[line_num] = line

            if len(matches) > 0:
                print(f"\n{len(matches)} match(s) found in file: {file}")
                print(matches)
            else:
                print(f"No match found in file {file}")


def main(arguments):
    """ This is the main part of the program
        Param1: list of argumets from sys.argv
    """

    if len(arguments) < 2:  # Make sure user entered folder as runtime argument
        print_usage()
    else:
        folder = get_folder(arguments[1])

        files = get_files(folder)

        regex = get_regex()

        find_matches(folder, files, regex)


if __name__ == "__main__":
    main(sys.argv)
