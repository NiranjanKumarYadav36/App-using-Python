import PySimpleGUI as sg
import zip_extractor


sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.InputText(tooltip='archive file')
choose_button1 = sg.FileBrowse("Choose", key='archive')

label2 = sg.Text("Select destination folder:")
input2 = sg.InputText(tooltip='folder')
choose_button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output', text_color='Green')

c1 = sg.Column([[label1], [label2]])
c2 = sg.Column([[input1], [input2]])
c3 = sg.Column([[choose_button1], [choose_button2]])
c4 = sg.Column([[extract_button]])

window = sg.Window("Archive Extractor", layout=[[c1, c2, c3], [c4, output_label]])

while True:
    event, value = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Extract':
        try:
            archive_path = value['archive']
            dest_dir = value['folder']

            if archive_path and dest_dir:  # Check if both archive and destination are provided
                zip_extractor.extract_archive(archive_path, dest_dir)
                window['output'].update(f"Extraction Completed")
            else:
                sg.popup("Provide the archive and destination folder both")
        except FileNotFoundError:
            sg.popup("Error: File not found")

    window.close()

