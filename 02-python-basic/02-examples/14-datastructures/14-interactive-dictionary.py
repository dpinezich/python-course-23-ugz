"""
Example implementation of an interactive dictionary.

This implementation is kept as simple as possible and is tailored to the material presented during the Python Basics
course.
"""

EXIT_COMMAND = "exit"
INSERT_COMMAND = "insert"
DELETE_COMMAND = "delete"
UPDATE_COMMAND = "update"
LIST_COMMAND = "list"
HELP_COMMAND = "help"

print("=======================")
print("INTERACTIVE DICTIONARY")
print("=======================")
print()

dictionary = {}


def insert_entry():
    key = input("[INSERT] Please enter new key: ")
    value = input("[INSERT] Please enter the corresponding value: ")

    if key in dictionary:
        answer = input(
            f"[INSERT] There is already an entry with the key {key}! Overwrite (enter 'yes' or 'no')? ")

        if answer == "yes":
            dictionary[key] = value
            print(f"[INSERT] Entry with key '{key}' was added successfully!")
        else:
            print(f"[INSERT] Entry was NOT added.")
    else:
        dictionary[key] = value
        print(f"[INSERT] Entry with key '{key}' was successfully added!")


def delete_entry():
    if len(dictionary) == 0:
        input("[DELETE] There are currently no entries.")
        return

    key = input("[DELETE] Please enter the key of the entry to be deleted: ")

    if key not in dictionary:
        print(f"[DELETE] There is no entry with the key {key}.")
        return

    answer = input(
        f"[DELETE] An entry with the key {key} already exists! Delete ('yes' or 'no' enter)? ")

    if answer == "yes":
        del dictionary[key]
        print(f"[DELETE] Entry with the key '{key}' was successfully deleted!")
    else:
        print(f"[DELETE] Entry was NOT deleted.")


def update_entry():
    if len(dictionary) == 0:
        print("[UPDATE] Currently there are no entries.")
        return

    key = input("[UPDATE] Please enter the key of the entry which should be changed: ")

    if key not in dictionary:
        print(f"[UPDATE] There is no entry with the key {key}.")
        return

    new_value = input("[UPDATE] Please enter new value for the entry: ")

    dictionary[key] = new_value

    print(f"[UPDATE] Entry with key '{key}' has been updated successfully!")


def list_entries():
    if len(dictionary) == 0:
        print("[LIST] There are currently no entries.")
        return

    print("[LIST] The following entries are available in the dictionary:")

    for k, v in dictionary.items():
        print(f" > {k} -> {v}")


def show_help():
    print("""
[HELP] The available commands are:
    > 'help': Display help
    > 'insert': Add new entry to the dictionary
    > 'update': Update existing entry in the dictionary
    > 'delete': Delete existing entry from the dictionary
    > 'list': Show all dictionary entries
    > 'exit': Exit the dictionary
    """)


command = ""

while command != EXIT_COMMAND:
    command = input("Please enter command (e.g. 'help'): ")

    if command == INSERT_COMMAND:
        insert_entry()
    elif command == DELETE_COMMAND:
        delete_entry()
    elif command == UPDATE_COMMAND:
        update_entry()
    elif command == LIST_COMMAND:
        list_entries()
    elif command == HELP_COMMAND:
        show_help()
    else:
        if command != EXIT_COMMAND:
            print(f"[WARNING] The command '{command}' was NOT recognized! ")

print("[THE END] See ya!")
