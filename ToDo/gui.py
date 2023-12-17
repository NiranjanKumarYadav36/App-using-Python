import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


sg.theme("GreenTan")

clock_label = sg.Text('', key='time')

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=5)

show_items = sg.Listbox(values=functions.get_todos(), key='items', enable_events=True, size=[45, 10], text_color='Red')

edit_button = sg.Button("Edit", size=7)

complete_button = sg.Button("Complete")

exit_button = sg.Button('Exit')


# Window is a mother of all instances
# layout must contain list

window = sg.Window('ToDo-Do App',
                   layout=[[clock_label], [label, input_box, add_button], [show_items, edit_button, complete_button], [exit_button]],
                   font=('Melvetica', 10))

while True:
    event, value = window.read(timeout=200)
    window['time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(value)
    # print(value['items'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)

            functions.write_todos(todos)
            window['items'].update(values=todos)
        case 'Edit':
            try:
                selected_todo = value["items"][0]
                new_todo = value["todo"]

                current_todo = functions.get_todos()
                index = current_todo.index(selected_todo)
                current_todo[index] = new_todo + "\n"

                functions.write_todos(current_todo)
                window['items'].update(values=current_todo)
            except IndexError:
                sg.popup("Please Select an item first", font=('Helvetica', 10))
        case 'Complete':
            try:
                todo_to_complete = value['items'][0]
                # print(todo_to_complete)
                todos = functions.get_todos()

                index = todos.index(todo_to_complete)
                # print(index)

                todos.pop(index)
                # print(todos)

                functions.write_todos(todos)
                window['items'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please Select an item first", font=('Helvetica', 10))
        case 'Exit':
            break
        case 'items':
            window['todo'].update(value=value['items'][0])

        case sg.WIN_CLOSED:
            break

window.close()






