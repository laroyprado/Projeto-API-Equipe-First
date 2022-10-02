from sre_constants import IN
import PySimpleGUI as sg # Importação da ferramenta PySimpleGUI, após o comando "as" podemos definir o apelido "sg" para que seja mais rápido e facil usar a biblioteca
#import pandas as pd #Importação da ferramenta Pandas, definindo o apelido "pd"

sg.theme('LightGreen1') # Aqui definimos o tema que será usado no layout
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
#class administrador():
def fun_adm():
    layout_adm = [
        [sg.Text('Bem vindo fulano', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.pin(sg.Button('Consultar alunos',
        font=('Arial',20),  key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', font=('Arial',20),  key='-NOTAS-')),
        sg.pin(sg.Button('Classificar notas', font=('Arial',20),  key='-RANK-'))]
    ]
    return sg.Window('ADMINISTRADOR', layout=layout_adm, margins=(10, 10), finalize=True)
#adm = fun_adm() 

#class adm_alunos():
def fun_adm_alunos():
    layout_adm_alnos = [
        [sg.Text('Bem vindo aaaa', expand_x=True, justification='center', font=('Arial', 20))],
        [sg.pin(sg.Button('Consultar alunos', font=('Arial',20),  key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', font=('Arial',20),  key='-NOTAS-')),
        sg.pin(sg.Button('Classificar notas', font=('Arial',20),  key='-RANK-'))],
        [sg.Button('Retornar', expand_x=True, font=('Arial', 20), key='-ToADM-')]
    ]
    return sg.Window('ALUNOS', layout=layout_adm_alnos, margins=(10, 10), finalize=True)
#admaluno = fun_adm_alunos() 
janela1, janela2 = fun_adm(), None

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
    elif window == janela2 and eventos in ['-ToADM-']:
        janela1 = fun_adm()
        janela2.hide()
 
