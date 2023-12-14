FILEPATH = "todos.txt"

# parameter
# non default parameters is placed before default parameters


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

# doc strings

# print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text field. """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

# value of __name__ will be main when we run functions program
# print(__name__)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
