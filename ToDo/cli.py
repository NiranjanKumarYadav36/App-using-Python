
# local module
import functions
# standard module
import time


now = time.strftime("%b %d, %Y %H:%H:%S")
print("It is ", now)

while True:
    # get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # if 'add' not in user_action or "new" in user_action: BOOLEAN OPERATOR

    if user_action.startswith("add"):
        # Get the to-do item without the 'add' keyword
        todo = user_action[4:]

        # Add a newline character to the to-do item
        todo += "\n"

        # Context manager to read existing todos
        # argument
        todos = functions.get_todos()

        # Append the new todo
        todos.append(todo)

        # Context manager to write todos back to the file

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            final = f"{index + 1}--{item}"
            print(final)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new = input("Enter new todo: ")
            todos[number] = new + "\n"

            functions.write_todos(todos, "todos.txt")

        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(filepath="todos.txt", todos_arg=todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")


print("Thank You")