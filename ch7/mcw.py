#! python3
# mcb.py Saves and loads pieces of text to the clipboard
# Usage:
# python mcb.py save <keyword> - Saves clipboard to keyword
# python mcb.py <keyword> - Loads keyword data to clipboard
# python mcb.py list - Lists all of the stored keywords

import shelve, sys, pyperclip


def print_usage():
    """ Print the usage information of the the program """

    print(
        """
    Usage:
    python mcb.py save <keyword> - Saves clipboard to keyword
    python mcb.py <keyword> - Loads keyword data to clipboard
    python mcb.py delete <keyword> - Deletes the data associated with keyword
    python mcb.py delete-all <keyword> - Deletes all data
    python mcb.py list - Lists all of the stored keywords"""
    )


def save_entry(database):
    """ Save data from the clipboard with the keywoard listed from sys.argv """
    """ Param1 database: expects an open shelve object """

    database[sys.argv[2].lower()] = pyperclip.paste()


def list_keys(database):
    """ List all of the keys from the opened shelve object """
    """ Param1 database: expects an open shelve object """

    print(f"List of Stored Keys:")

    for key in database.keys():
        print(f"- {key}")


def fetch_data(database):
    """ Take the sys.argv, try to find its key in the database, print the value and copy to clipboard """
    """ Param1 database: expects an open shelve object """

    try:
        print(database[sys.argv[1].lower()])
        pyperclip.copy(database[sys.argv[1].lower()])
    except KeyError:
        print("Entry not found in database")


def delete_entry(database):
    """ Take the sys.argv, try to find its key in the database, print the value and copy to clipboard """
    """ Param1 database: expects an open shelve object """

    try:
        del database[sys.argv[2].lower()]
        print(f" Entry: {sys.argv[2].lower()} deleted.")
    except KeyError:
        print(f"Unable to delete entry")


def delete_all(database):
    """ Deletes all data from the database """
    """ Param1 database: expects an open shelve object """

    try:
        for key in database.keys():
            print(f"Deleting: {key}")
            del database[key]
    except:
        print(f"No keys to delete or other error")


try:
    with shelve.open("mcb.db") as mcb_db:

        if len(sys.argv) <= 1:
            print_usage()

        elif len(sys.argv) == 3 and sys.argv[1].lower() == "save":
            save_entry(mcb_db)

        elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
            delete_entry(mcb_db)

        elif len(sys.argv) == 2:

            if sys.argv[1].lower() == "list":
                list_keys(mcb_db)
            elif sys.argv[1].lower() == "delete-all":
                delete_all(mcb_db)
            else:
                fetch_data(mcb_db)

except EnvironmentError:
    print(f"File cannot be accessed")

