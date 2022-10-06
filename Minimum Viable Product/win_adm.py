from sre_constants import IN
from types import NoneType
import PySimpleGUI as sg # Importação da ferramenta PySimpleGUI, após o comando "as" podemos definir o apelido "sg" para que seja mais rápido e facil usar a biblioteca
import pandas as pd #import pandas as pd #Importação da ferramenta Pandas, definindo o apelido "pd"

sg.theme('LightGreen1') # Aqui definimos o tema que será usado no layout

def fun_login():
    layout_login = [
    [sg.Text('Usuário',font=('Arial', 15))],[sg.Input(font=('Arial', 15), key='usuário', size=(30,30))],
    [sg.Text('Senha',font=('Arial', 15))], [sg.Input(font=('Arial', 15), key='senha', password_char= '*', size=(26,30)), sg.Button('Ver', font=('Arial', 10), size=(3,1))],
    [sg.Button('Entrar',font=('Arial',17))]
    ]
    return sg.Window('Tela de Login', layout=layout_login, margins=(20,20),finalize=True)

'''
class First(): # Criação da classe
    def fun_matricula(): # Criação da função
        layout_cadastro = [ # Criação da tela, especificando tamanho, fonte e KEY que é fundamental para o funcionamento do programa
            [sg.Text('Matrícula', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-MATRICULA-')],
            [sg.Text('Nome', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-NOME-')],
            [sg.Text('Senha', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-SENHA-')],
            [sg.Text('Time', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-TIME-'),
            sg.Text('Cargo', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-CARGO-')],
            [sg.Button('Confirmar', expand_x=True, font=('Arial', 20), key='-CONFIRMAR-')]
        ]
        return sg.Window('Cadastro', layout=layout_cadastro, margins=(10, 10), finalize=True) # Aqui estamos criando o comando para que a janela seja criada quando a função for executada
    matricula = fun_matricula() # Aqui estamos definindo a variavel "matricula" como respondavel pelo funcionamento da função "fun_matricula"
'''   
#função administrador():
def fun_adm():
    layout_adm = [
        [sg.Text('Bem vindo ADM', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.pin(sg.Button('Consultar alunos',font=('Arial',20),  key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', font=('Arial',20),  key='-TIMES-')),
        sg.pin(sg.Button('Classificar notas', font=('Arial',20),  key='-NOTAS-'))]
    ]
    return sg.Window('ADMINISTRADOR', layout=layout_adm, margins=(10, 10), finalize=True)
#adm = fun_adm() 

#class adm_alunos():
def fun_consultar():
    layout_consultar = [
        [sg.Text('Bem vindo', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.pin(sg.Button('Consultar alunos', font=('Arial',20),  key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', font=('Arial',20),  key='-TIMES-')),
        sg.pin(sg.Button('Classificar notas', font=('Arial',20),  key='-NOTAS-'))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('ALUNOS', layout=layout_consultar, margins=(10, 10), finalize=True)

#admaluno = fun_adm_alunos() 
win_login, win_aluno, win_prof, win_adm, con_cads, con_times, con_notas, win_cad = None, None, None, fun_adm() ,None, None, None, None

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
        con_cads = fun_consultar()
        con_cads.un_hide()
        win_adm.hide()
    elif window == win_adm and eventos in ['-TIMES-']:
        con_times = fun_consultar()
        con_times.un_hide()
        win_adm.hide()
    elif window == win_adm and eventos in ['-NOTAS-']:
        con_notas = fun_consultar()
        con_notas.un_hide()
        win_adm.hide()
 
