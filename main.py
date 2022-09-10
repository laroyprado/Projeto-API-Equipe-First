import PySimpleGUI as sg
import pandas as pd

sg.theme('LightGreen1')

class First():
    def fun_login():
        layout_login = [
        ]
    
    def fun_aluno():
        layout_aluno =[

        ]
    def fun_instrutor():
        layout_instrutor =[

        ]
    def fun_admin():
        layout_admin =[
        ]

    def fun_matricula():
        layout_cadastro = [
            [sg.Text('Matrícula', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-MATRICULA-')],
            [sg.Text('Nome', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-NOME-')],
            [sg.Text('Senha', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-SENHA-')],
            [sg.Text('Time', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-TIME-'),
            sg.Text('Cargo', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-TURMA-')],
            [sg.Button('Confirmar', expand_x=True, font=('Arial', 20), key='-CONFIRMAR-')]
        ]
        return sg.Window('Cadastro', layout=layout_cadastro, margins=(10, 10), finalize=True)

    matricula = fun_matricula()

    while True:
        window, eventos, valores = sg.read_all_windows()

        if window == matricula and eventos == sg.WINDOW_CLOSED:
            break

First()