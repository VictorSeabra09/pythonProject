import PySimpleGUI as sg

layout = [

            [sg.Text('Incluit novo Cliente')],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('nome', key="it_nome")],
            [sg.Text('Endereco', size=(15, 1)), sg.InputText('endereco', key="it_endereco")],
            [sg.Submit(), sg.Cancel()]
        ]

window = sg.Window('Cadastro de Clientes').Layout(layout)

sg.theme_previewer()
#button, values = window.Read()
#print(button)
#print(values)
