""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    ui.print_menu(
        "HR",
        [
            "Show table",
            "Add",
            "Remove",
            "Update",
            "Who is the oldest person?",
            "Who is the closest to the average age?"
        ],
        "Back to main menu"
    )
    while True:
        inputs = input("Choose an option: ")
        option = inputs[0]
        file_name = "hr/persons.csv"
        if option == "1":
            show_table(data_manager.get_table_from_file(file_name))
        elif option == "2":
            add(data_manager.get_table_from_file(file_name))
        elif option == "3":
            id_ = ui.get_inputs(["ID: "], "Please provide added information")
            remove(data_manager.get_table_from_file(file_name), id_)
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please provide added information")
            update(data_manager.get_table_from_file(file_name), id_)
        elif option == "5":
            which_year_max(data_manager.get_table_from_file(file_name))
        elif option == "6":
            avg_amount(data_manager.get_table_from_file(file_name), year)
        elif option == "0":
            return
        else:
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    hr_title = ["ID", "Name", "Birth year"]
    file_name = "hr/persons.csv"

    ui.print_table(data_manager.get_table_from_file(file_name), hr_title)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    user_inputs = ["Name: ", "Birth year: "]
    hr_add_table = [common.generate_random(table)]

    # to common.py?
    while True:
        try:
            given_inputs = ui.get_inputs(user_inputs, "Please provide added information")
            given_inputs[1] = int(given_inputs[1])  # birth year validation
            if given_inputs[1] in range(1900, 2020):
                given_inputs[1] = str(given_inputs[1])  # conversion to string for filewriteing
                break
            else:
                print("Type in a valid year!\n")
        except ValueError:
            print("Type in a year with numbers!\n")

    hr_add_table.extend(given_inputs)  # put new item to table
    table.extend([hr_add_table])

    data_manager.write_table_to_file("hr/persons.csv", table)  # write added item to file

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    table = data_manager.get_table_from_file(file_name="hr/persons.csv")
    for line in table:
        if id_ in line:
            table.remove(line)

    print(table)

    data_manager.write_table_to_file("hr/persons.csv", table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    print()
    user_choice = ui.get_inputs(["Which label do you want to update? (Name, Birth year): "],
                                "Please provide added information")
    for line in table:
        if id_ == line[0]:
            if user_choice == "Name":
                line[1] = ui.get_inputs(["New Name? "], "")
            if user_choice == "Birth year":
                line[2] = ui.get_inputs(["New Birth year? "], "")
            continue
        break
    else:
        print("No such ID!")

    data_manager.write_table_to_file("hr/persons.csv", table)

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code




# COMMON

""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    # must implement check if ID is unique
    for line in table:
        if generated == line[0] or generated == '':
            generated = ''.join(random.choice("!#$%&*+-?@^~") + random.choice("0123456789")
                                + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                                + random.choice("abcdefghijklmnopqrstuvwxyz") for e in range(2))
    return generated
