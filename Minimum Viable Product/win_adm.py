from sre_constants import IN
import PySimpleGUI as sg # Importação da lib PySimpleGUI como "sg"
import tkinter
import pandas as pd # Importação da lib pandas como "pd"

excel_header = ['Matricula', 'Nome','Senha','Time','Cargo'] # Aqui estamos informando os nomes das colunas
cadastro_df = pd.DataFrame(data = pd.read_excel(r'C:\Users\danko\OneDrive\Documentos\GitHub\Projeto-API-Equipe-First\DataBase\arquivo.xlsx', engine='openpyxl'), columns=excel_header) # Aqui estamos criando um DataFrame com as informações do arquivo excel, mudar o endereco da pasta

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
    nomes = cadastro_df['Nome']

    layout_adm_alnos = [
        [sg.Text('ALUNOS CADASTRADOS:', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Listbox(cadastro_df['Nome'], expand_x=True, size=(20, 5), font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('ALUNOS', layout=layout_adm_alnos, margins=(10, 10), finalize=True)

def fun_adm_times(): #Criação da tela de consulta da lista de times
    layout_adm_alnos = [
        [sg.Text(cadastro_df.loc[:,'Time'], expand_x=True, justification='center', font=('Arial', 20))],
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
        con_times = fun_adm_alunos()
        win_adm.hide()
    if window == win_adm and eventos in ['-TIMES-']: #Navega da tela do adm para a tela de consulta de times 
        con_times = fun_adm_times()
        win_adm.hide()
    if window == win_adm and eventos in ['-NOTAS-']: #Navega da tela do adm para a tela da consulta de notas
        con_notas = fun_adm_notas()
        win_adm.hide()
    elif window == con_times and eventos in ['-ToADM-']: #Retorna para a pagina do adm
        win_adm = fun_adm()
        con_times.hide()
    elif window == con_times and eventos in ['-ToADM-']: #Retorna para a pagina do adm
        win_adm = fun_adm()
        con_times.hide()
    elif window == con_notas and eventos in ['-ToADM-']: #Retorna para a pagina do adm
        win_adm = fun_adm()
        con_notas.hide()