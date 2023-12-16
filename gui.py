import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

show_items = sg.Listbox(values=functions.get_todos(), key='items', enable_events=True, size=[45,10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button('Exit')

# Window is a mother of all instances
# layout must contain list

window = sg.Window('To-Do App',
                   layout=[[label, input_box, add_button], [show_items, edit_button, complete_button], [exit_button]],
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
        case 'Complete':
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
        case 'Exit':
            break
        case 'items':
            window['todo'].update(value=value['items'][0])

        case sg.WIN_CLOSED:
            break

window.close()














# exit() stops the progarm completely

# import functions
# import PySimpleGUI as sg
#
# label1 = sg.Text("Enter Todo")
# user_input = sg.InputText(key='todo')
# add_button = sg.Button("Add")
#
# show_items = sg.Listbox(values=functions.get_todos(), key='item', enable_events=True, size=[45,8])
# edit_button = sg.Button("Edit")
#
#
# window = sg.Window("TO do App", layout=[[label1, user_input, add_button], [show_items, edit_button]])
#
# while True:
#     event, value = window.read()
#     print(event)
#     print(value)
#     print(value['item'])
#
#     match event:
#         case 'Add':
#             todo_to_add = value['todo'] + '\n'
#             todos = functions.get_todos()
#
#             todos.append(todo_to_add)
#
#             functions.write_todos(todos)
#             window['item'].update(values=todos)
#         case 'Edit':
#             todo_to_edit = value['item'][0]
#             new_todo = value['todo']
#
#             current_todos = functions.get_todos()
#             index = current_todos.index(todo_to_edit)
#
#             current_todos[index] = new_todo + "\n"
#
#             functions.write_todos(current_todos)
#             window['item'].update(values=current_todos)
#         case 'item':
#             window['todo'].update(value=value['item'][0])
#
#         case sg.WIN_CLOSED:
#             break
#
# window.close()
