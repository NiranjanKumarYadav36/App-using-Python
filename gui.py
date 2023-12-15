import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# Window is a mother of all instances
# layout must contain list

window = sg.Window('To-Do App', layout=[[label, input_box, add_button]])
window.read()
window.close()

