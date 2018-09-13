#! python3
# regex-search.py - searches files in a folder for matches to a user provided regex

import sys, re, os


def print_usage():
    """ This function will print the usage information if too few command-line arguments are given """
    print(f"Usage:")
    # TODO: finish usage info


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
    """ This function will read the files in the folder one-by-one
        Returns: Compiled regex object
    """
    pattern = input("Please enter a regex pattern to search for: ")
    regex = re.compile(pattern)
    print(regex.pattern)
    return regex


def main():
    """ This is the main part of the program """

    if len(sys.argv) <= 1:  # Make sure user entered folder as runtime argument
        print_usage()
    else:
        folder = get_folder(sys.argv[1])

    files = get_files(folder)

    regex = get_regex()

    os.chdir(folder)
    for file in files:
        with open(file, "r") as f:
            contents = f.readlines()

            for line in contents:
                match = regex.search(line)
                if match:
                    print(f"\n\nMatch found on the following line:")
                    print(line)

            else:
                print(f"No Match")


if __name__ == "__main__":
    main()
