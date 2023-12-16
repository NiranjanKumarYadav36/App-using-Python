import PySimpleGUI as sg

import meter_converter

sg.theme('Black')

label1 = sg.Text("Enter feet:")
feet_input = sg.InputText(tooltip='Feet',key='feet')

label2 = sg.Text("Enter inches:")
inches_input = sg.InputText(tooltip='Inches', key='inches')

convert_button = sg.Button('Convert')

result_label = sg.Text(key='result', text_color='Green')

c1 = sg.Column([[label1], [label2]])
c2 = sg.Column([[feet_input], [inches_input]])


window = sg.Window("Converter", layout=[[c1, c2], [convert_button, result_label]])

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