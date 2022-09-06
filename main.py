import PySimpleGUI as sg
import pandas as pd

sg.theme('LightGreen1')

class First():
    def __init__():               
        layout_principal = [
            [sg.Button('Matricular', font=('Arial', 20), key='-4-')]
        ]
        return sg.Window('FIRST', layout=layout_principal, margins=(50,50), finalize=True)
    
    def fun_matricula():
        layout_cadastro = [
            [sg.Text('Matrícula', expand_x=True, font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-MATRICULA-')],
            [sg.Text('Nome', expand_x=True, font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-NOME-')],
            [sg.Text('Senha', expand_x=True, font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-SENHA-')],
            [sg.Text('Turma', expand_x=True, font=('Arial', 20)), sg.Combo('A B C D', expand_x=True, font=('Arial', 20), key='-TURMA-')],
            [sg.Button('Confirmar', expand_x=True, font=('Arial', 20))]
        ]
        return sg.Window('Matrícula', layout=layout_cadastro, margins=(10, 10), finalize=True)

    principal, matricula, login = __init__(), None, None

    while True:
        window, eventos, valores = sg.read_all_windows()
        
        if window == principal and eventos == sg.WIN_CLOSED:
            break

        if window == principal and eventos in ['-4-']:
            principal.hide()
            matricula = fun_matricula()

        if window == matricula and eventos == sg.WINDOW_CLOSED:
            break

First()