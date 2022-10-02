from sre_constants import IN
import PySimpleGUI as sg # Importação da ferramenta PySimpleGUI, após o comando "as" podemos definir o apelido "sg" para que seja mais rápido e facil usar a biblioteca
#import pandas as pd #Importação da ferramenta Pandas, definindo o apelido "pd"

sg.theme('LightGreen1') # Aqui definimos o tema que será usado no layout

def fun_adm():
    layout_adm = [
        [sg.Text('Bem vindo fulano', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.pin(sg.Button('Consultar alunos',font=('Arial',20),  key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', font=('Arial',20),  key='-TIMES-')),
        sg.pin(sg.Button('Classificar notas', font=('Arial',20),  key='-RANK-'))]
    ]
    return sg.Window('MINISTRADOR', layout=layout_adm, margins=(10, 10), finalize=True)

def fun_adm_alunos():
    layout_adm_alnos = [
        [sg.Text('CRUZAR OS ALUNOS NO PANDAS', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('ALUNOS', layout=layout_adm_alnos, margins=(10, 10), finalize=True)

def fun_adm_times():
    layout_adm_alnos = [
        [sg.Text('CRUZAR OS TIMES NO PANDAS', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('TIMES', layout=layout_adm_alnos, margins=(10, 10), finalize=True)

def fun_adm_rank():
    layout_adm_alnos = [
        [sg.Text('CRUZAR AS NOTAS NO PANDAS', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('TIMES', layout=layout_adm_alnos, margins=(10, 10), finalize=True)

janela1, janela2, janela3, janela4 = fun_adm(), None, None, None

while True: # Este comando serve para iniciar uma repetição, para que o programa funcione continuamente
    window, eventos, valores = sg.read_all_windows() 
    # Este comando a cima serve para armazenar as informações de qual janela está aberta no momento, qual evento foi realizado e também qual valor foi inserido
        # window = serve para especificar a janela que está aberta no momento
        # eventos = serve para capturar alguma ação realizada na janela, como clicar em algum botão
        # valores = serve para receber o valor de um input, ou alguma outra forma de o usuário inserir infromações
    
    if eventos == sg.WINDOW_CLOSED: # Aqui estamos especificando o que será feito quando clicar no X da janela sendo "sg.WINDOW_CLOSE" o evento
        break # Este comando serve para encerrar uma repetição
    if window == janela1 and eventos in ['-ALUNOS-']:
        janela2 = fun_adm_alunos()
        janela1.hide()
    if window == janela1 and eventos in ['-TIMES-']:
        janela3 = fun_adm_times()
        janela1.hide()
    if window == janela1 and eventos in ['-RANK-']:
        janela4 = fun_adm_rank()
        janela1.hide()
    elif window == janela2 and eventos in ['-ToADM-']:
        janela1 = fun_adm()
        janela2.hide()
    elif window == janela3 and eventos in ['-ToADM-']:
        janela1 = fun_adm()
        janela3.hide()
    elif window == janela4 and eventos in ['-ToADM-']:
        janela1 = fun_adm()
        janela4.hide()