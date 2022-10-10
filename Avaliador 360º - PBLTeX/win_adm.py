import linecache
from sre_constants import IN
import PySimpleGUI as sg # Importação da lib PySimpleGUI como "sg"
import tkinter
import pandas as pd # Importação da lib pandas como "pd"

excel_header = ['Matricula', 'Nome','Senha','Time','Cargo'] # Aqui estamos informando os nomes das colunas
cadastro_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'), columns=excel_header) # Aqui estamos criando um DataFrame com as informações do arquivo excel, mudar o endereco da pasta
nome = []

sg.theme('LightGreen1') # Aqui definimos o tema que será usado no layout

def fun_adm(): #Criação da tela principal do administrador
    layout_adm = [
        [sg.Text('Bem vindo', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.pin(sg.Button('Consultar alunos',font=('Arial',20),  key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', font=('Arial',20),  key='-TIMES-')),
        sg.pin(sg.Button('Consultar notas', font=('Arial',20),  key='-NOTAS-'))]
    ]
    return sg.Window('ADMINISTRADOR', layout=layout_adm, margins=(10, 10), finalize=True)

def fun_adm_alunos(): #Criação da tela de consulta da lista de alunos
    nome.clear()
    for linha in cadastro_df['Nome']:
            nome.append(linha)
    layout_adm_alnos = [
        [sg.Text('ALUNOS CADASTRADOS:', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Combo(nome, expand_x=True, size=(20, 5), font=('Arial', 20), key='-SELECT-')],
        [sg.Text('Matrícula', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-MATRICULA-')],
        [sg.Text('Nome', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-NOME-')],
        [sg.Text('Senha', font=('Arial', 20)), sg.Input('', font=('Arial', 20), password_char='*', key='-SENHA-')],
        [sg.Text('Time', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-TIME-'),
        sg.Text('Cargo', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-CARGO-')],
        [sg.Button('Consultar', expand_x=True, font=('Arial', 20), key='-CONSULTAR-'),
        sg.Button('Alterar', expand_x=True, font=('Arial', 20), key='-ALTERAR-'),
        sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('ALUNOS', layout=layout_adm_alnos, margins=(10, 10), finalize=True)

def fun_adm_times(): #Criação da tela de consulta da lista de times
    layout_adm_alnos = [
        [sg.Listbox(cadastro_df['Time'], size=(15, 5), font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('TIMES', layout=layout_adm_alnos, margins=(10, 10), finalize=True)

def fun_adm_notas(): #Criação da tela de consulta das notas 
    layout_adm_alnos = [
        [sg.Text('CRUZAR AS NOTAS NO PANDAS', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('NOTAS', layout=layout_adm_alnos, margins=(10, 10), finalize=True)

win_adm, con_alunos, con_times, con_notas = fun_adm(), None, None, None

while True: # Este comando serve para iniciar uma repetição, para que o programa funcione continuamente
    window, eventos, valores = sg.read_all_windows() 
    # Este comando a cima serve para armazenar as informações de qual janela está aberta no momento, qual evento foi realizado e também qual valor foi inserido
        # window = serve para especificar a janela que está aberta no momento
        # eventos = serve para capturar alguma ação realizada na janela, como clicar em algum botão
        # valores = serve para receber o valor de um input, ou alguma outra forma de o usuário inserir infromações
    
    if eventos == sg.WINDOW_CLOSED: # Aqui estamos especificando o que será feito quando clicar no X da janela sendo "sg.WINDOW_CLOSE" o evento
        break # Este comando serve para encerrar uma repetição
    if window == win_adm and eventos in ['-ALUNOS-']: #Navega da pagina do adm para a pagina de consulta dos alunos
        win_adm.hide()
        con_alunos = fun_adm_alunos()
    if window == con_alunos and eventos in ['-CONSULTAR-']:
        x = 0
        for linha in cadastro_df['Nome']:
            if linha == valores['-SELECT-']:
                window['-MATRICULA-'].update(value=cadastro_df.loc[x].at['Matricula'])
                window['-NOME-'].update(value=cadastro_df.loc[x].at['Nome'])
                window['-SENHA-'].update(value=cadastro_df.loc[x].at['Senha'])
                window['-TIME-'].update(value=cadastro_df.loc[x].at['Time'])
                window['-CARGO-'].update(value=cadastro_df.loc[x].at['Cargo'])
            x += 1
    if window == con_alunos and eventos in ['-ALTERAR-']:
        x = 0
        for linha in cadastro_df['Matricula']:
            if valores['-MATRICULA-'] == '':
                sg.popup_ok('Campo vazio')
            elif valores['-MATRICULA-'] == str(linha):
                cadastro_df.at[x, 'Matricula'] = valores['-MATRICULA-']
                cadastro_df.at[x, 'Nome'] = valores['-NOME-']
                cadastro_df.at[x, 'Senha'] = valores['-SENHA-']
                cadastro_df.at[x, 'Time'] = valores['-TIME-']
                cadastro_df.at[x, 'Cargo'] = valores['-CARGO-']
                writer = pd.ExcelWriter('Avaliador 360º - PBLTeX/arquivo.xlsx')
                cadastro_df.to_excel(writer)
                writer.save()
                con_alunos.close()
                con_alunos = fun_adm_alunos()
            x += 1
    if window == win_adm and eventos in ['-TIMES-']: #Navega da tela do adm para a tela de consulta de times
        win_adm.hide()
        con_times = fun_adm_times()
    if window == win_adm and eventos in ['-NOTAS-']: #Navega da tela do adm para a tela da consulta de notas
        win_adm.hide()
        con_notas = fun_adm_notas()
    elif window == con_alunos and eventos in ['-ToADM-']: #Retorna para a pagina do adm
        con_alunos.hide()
        win_adm = fun_adm()
    elif window == con_times and eventos in ['-ToADM-']: #Retorna para a pagina do adm
        con_times.hide()
        win_adm = fun_adm()
    elif window == con_notas and eventos in ['-ToADM-']: #Retorna para a pagina do adm
        con_notas.hide()
        win_adm = fun_adm()
