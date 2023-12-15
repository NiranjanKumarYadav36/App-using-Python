import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

show_items = sg.Listbox(values=functions.get_todos(), key='items', enable_events=True, size=[45,10])

edit_button = sg.Button("Edit")

# Window is a mother of all instances
# layout must contain list

window = sg.Window('To-Do App',
                   layout=[[label, input_box, add_button], [show_items, edit_button]],
                   font=('Melvetica', 10))

while True:
    event, value = window.read()
    print(event)
    print(value)
    print(value['items'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['items'].update(values=todos)
        case 'Edit':
            selected_todo = value["items"][0]
            new_todo = value["todo"]

            current_todo = functions.get_todos()
            index = current_todo.index(selected_todo)
            current_todo[index] = new_todo + "\n"

            functions.write_todos(current_todo)
            window['items'].update(values=current_todo)
        case 'items':
            window['todo'].update(value=value['items'][0])

        case sg.WIN_CLOSED:
            break

window.close()

