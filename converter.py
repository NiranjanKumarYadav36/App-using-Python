import PySimpleGUI as sg

import meter_converter

sg.theme('Black')

label1 = sg.Text("Enter feet:")
feet_input = sg.InputText(key='feet')

label2 = sg.Text("Enter inches:")
inches_input = sg.InputText(key='inches')

convert_button = sg.Button('Convert')

result_label = sg.Text(key='result', text_color='Green')

window = sg.Window("Converter", layout=[[label1, feet_input], [label2, inches_input], [convert_button, result_label]])

while True:
    event, value = window.read()
    # print(event)
    # print(value)

    match event:
        case 'Convert':
            try:
                feet = float(value['feet'])
                inches = float(value['inches'])
                # print(feet, inches)

                answer = meter_converter.result(feet, inches)

                window['result'].update(f"{answer} m")
            except ValueError:
                sg.popup("Enter the value first")
        case sg.WIN_CLOSED:
            break

window.close()