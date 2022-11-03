import PySimpleGUI as sg

sg.theme('LightGreen1')
sg.set_options(font=('Arial', 50))

layout = [
    [sg.Text('Insira um número'), sg.Input(key='number', size=(20, 1))], 
    [sg.ProgressBar(10, orientation='h', size=(20, 20), border_width=1, key='bar')],
    [sg.Button('Mostrar progresso', key='mostrar')],
]

window = sg.Window('Progress Bar', layout)

while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos in ['mostrar']:
        progresso = int(valores['number'])
        if progresso <= 4:
            window['bar'].update(progresso, bar_color=('red', 'white'))
        elif progresso > 4 and progresso < 8:
            window['bar'].update(progresso, bar_color=('yellow', 'white'))
        if progresso >= 8:
            window['bar'].update(progresso, bar_color=('green', 'white'))