import PySimpleGUI as sg
import pandas as pd

sg.theme('LightGreen1')

class First():
    def fun_matricula():
        menu_cadastro = [
            ['Adicionar', ['Turma', 'Cargo']],
        ]
        layout_cadastro = [
            [sg.Menu(menu_cadastro)],
            [sg.Text('Matrícula', expand_x=True, font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-MATRICULA-')],
            [sg.Text('Nome', expand_x=True, font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-NOME-')],
            [sg.Text('Senha', expand_x=True, font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-SENHA-')],
            [sg.Text('Turma', expand_x=True, font=('Arial', 20)), sg.Combo('A B C D', expand_x=True, font=('Arial', 20), key='-TURMA-'),
            sg.Text('Cargo', expand_x=True, font=('Arial', 20)), sg.Combo('Aluno Professor Coordenador', expand_x=True, font=('Arial', 20), key='-TURMA-')],
            [sg.Button('Confirmar', expand_x=True, font=('Arial', 20))]
        ]
        return sg.Window('Matrícula', layout=layout_cadastro, margins=(10, 10), finalize=True)

    matricula, login = fun_matricula(), None

    while True:
        window, eventos, valores = sg.read_all_windows()

        if window == matricula and eventos == sg.WINDOW_CLOSED:
            break

First()