import PySimpleGUI as sg
import pandas as pd

sg.theme('LightGreen1')

class First():
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
        excel_header = ['Matricula', 'Nome','Senha','Time','Turma']
        cadastro_df = pd.DataFrame(data = pd.read_excel('arquivo.xlsx', engine='openpyxl'), columns=excel_header)
    
        
        if window == matricula and eventos == sg.WINDOW_CLOSED: 
            break
       
        if window == matricula and eventos in ['-CONFIRMAR-']:
            if valores['-MATRICULA-'] and valores['-NOME-'] and valores['-SENHA-'] and valores['-TIME-'] and valores['-TURMA-'] != '':
                l = cadastro_df['Matricula'].count()
                cadastro_df.loc[l+1] = ([valores['-MATRICULA-']] + [valores['-NOME-']] + [valores['-SENHA-']] + [valores['-TIME-']] + [valores['-TURMA-']])
                writer = pd.ExcelWriter('arquivo.xlsx')
                cadastro_df.to_excel(writer)
                writer.save()
                matricula.close()
                matricula = fun_matricula()
                sg.popup_quick("Cadastrado com sucesso!")
            else:
                sg.popup_quick("Necessario preencher todos os campos!")
First()