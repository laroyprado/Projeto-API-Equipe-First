import PySimpleGUI as sg # Importação da ferramenta PySimpleGUI, após o comando "as" podemos definir o apelido "sg" para que seja mais rápido e facil usar a biblioteca
import pandas as pd #Importação da ferramenta Pandas, definindo o apelido "pd"

sg.theme('LightGreen1') # Aqui definimos o tema que será usado no layout

class First(): # Criação da classe
    def fun_matricula(): # Criação da função
        layout_cadastro = [ # Criação da tela, especificando tamanho, fonte e KEY que é fundamental para o funcionamento do programa
            [sg.Text('Matrícula', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-MATRICULA-')],
            [sg.Text('Nome', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-NOME-')],
            [sg.Text('Senha', font=('Arial', 20)), sg.Input('', font=('Arial', 20), key='-SENHA-')],
            [sg.Text('Time', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-TIME-'),
            sg.Text('Cargo', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-TURMA-')],
            [sg.Button('Confirmar', expand_x=True, font=('Arial', 20), key='-CONFIRMAR-')]
        ]
        return sg.Window('Cadastro', layout=layout_cadastro, margins=(10, 10), finalize=True)
        # Aqui estamos criando o comando para que a janela seja criada quando a função for executada

    matricula = fun_matricula()
    # Aqui estamos definindo a variavel "matricula" como respondavel pelo funcionamento da função "fun_matricula"

    while True: # Este comando serve para iniciar uma repetição, para que o programa funcione continuamente
        window, eventos, valores = sg.read_all_windows()        
        # Este comando a cima serve para armazenar as informações de qual janela está aberta no momento, qual evento foi realizado e também qual valor foi inserido
        # window = serve para especificar a janela que está aberta no momento
        # eventos = serve para capturar alguma ação realizada na janela, como clicar em algum botão
        # valores = serve para receber o valor de um input, ou alguma outra forma de o usuário inserir infromações

        if window == matricula and eventos == sg.WINDOW_CLOSED: # Aqui estamos especificando o que será feito quando clicar no X da janela sendo "sg.WINDOW_CLOSE" o evento
            break # Este comando serve para encerrar uma repetição

First() # Este comando serve para que a classe seja executada