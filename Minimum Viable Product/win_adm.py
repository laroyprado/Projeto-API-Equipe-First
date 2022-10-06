import PySimpleGUI as sg # Importação da ferramenta PySimpleGUI, após o comando "as" podemos definir o apelido "sg" para que seja mais rápido e facil usar a biblioteca
import pandas as pd #import pandas as pd #Importação da ferramenta Pandas, definindo o apelido "pd"

excel_header = ['Matricula', 'Nome','Senha','Time','Cargo'] # Aqui estamos informando os nomes das colunas
cadastro_df = pd.DataFrame(data = pd.read_excel(r'C:\Users\danko\OneDrive\Documentos\GitHub\Projeto-API-Equipe-First\DataBase\arquivo.xlsx', engine='openpyxl'), columns=excel_header) # Aqui estamos criando um DataFrame com as informações do arquivo excel, mudar o endereco da pasta

sg.theme('LightGreen1') # Aqui definimos o tema que será usado no layout

#função administrador():
def fun_adm():
    layout_adm = [
        [sg.Text('Bem vindo ADM', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.pin(sg.Button('Consultar alunos',font=('Arial',20),  key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', font=('Arial',20),  key='-TIMES-')),
        sg.pin(sg.Button('Classificar notas', font=('Arial',20),  key='-NOTAS-'))]
    ]
    return sg.Window('ADMINISTRADOR', layout=layout_adm, margins=(10, 10), finalize=True)

def fun_cons_aluno():
    layout_consultar = [
        [sg.Text(cadastro_df.loc[:,'Nome'], expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('ALUNOS', layout=layout_consultar, margins=(10, 10), finalize=True)

def fun_cons_times():
    layout_consultar = [
        [sg.Text(cadastro_df.loc[:,'Time'], expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('ALUNOS', layout=layout_consultar, margins=(10, 10), finalize=True)

def fun_cons_notas():
    layout_consultar = [
        [sg.Text('', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('ALUNOS', layout=layout_consultar, margins=(10, 10), finalize=True)

win_adm, con_alunos, con_times, con_notas = fun_adm() ,None, None, None

# win_login é a tela de login, #win_aluno é a tela do aluno, #win_prof é a tela do prof, #con_cads é a tela de consulta cadastros, #con_times é a tela de consulta de times, #con_notas é a tela de consultas de notas, #win_cad é a tela de cadastro 

while True: # Este comando serve para iniciar uma repetição, para que o programa funcione continuamente
    window, eventos, valores = sg.read_all_windows() 

        # Este comando a cima serve para armazenar as informações de qual janela está aberta no momento, qual evento foi realizado e também qual valor foi inserido
        # window = serve para especificar a janela que está aberta no momento
        # eventos = serve para capturar alguma ação realizada na janela, como clicar em algum botão
        # valores = serve para receber o valor de um input, ou alguma outra forma de o usuário inserir informações
    
    if eventos == sg.WINDOW_CLOSED: # Aqui estamos especificando o que será feito quando clicar no X da janela sendo "sg.WINDOW_CLOSE" o evento
        break # Este comando serve para encerrar uma repetição

    if window == win_adm and eventos in ['-ALUNOS-']:
        win_adm.hide()
        con_alunos = fun_cons_aluno()
    if window == win_adm and eventos in ['-TIMES-']:
        win_adm.hide()
        con_times = fun_cons_times()
    if window == win_adm and eventos in ['-NOTAS-']:
        win_adm.hide() 
        con_notas = fun_cons_notas()
    if window != win_adm and eventos in ['-ToADM-']:
        con_alunos.hide()
        con_times.hide()
        con_notas.hide()
        win_adm.un_hide()