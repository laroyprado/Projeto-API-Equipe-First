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
            sg.Text('Cargo', size=(10), font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-CARGO-')],
            [sg.Button('Confirmar', expand_x=True, font=('Arial', 20), key='-CONFIRMAR-')]
        ]
        return sg.Window('Cadastro', layout=layout_cadastro, margins=(10, 10), finalize=True) # Aqui estamos criando o comando para que a janela seja criada quando a função for executada

    matricula = fun_matricula() # Aqui estamos definindo a variavel "matricula" como respondavel pelo funcionamento da função "fun_matricula"

    while True: # Este comando serve para iniciar uma repetição, para que o programa funcione continuamente
        window, eventos, valores = sg.read_all_windows()        
        # Este comando a cima serve para armazenar as informações de qual janela está aberta no momento, qual evento foi realizado e também qual valor foi inserido
        # window = serve para especificar a janela que está aberta no momento
        # eventos = serve para capturar alguma ação realizada na janela, como clicar em algum botão
        # valores = serve para receber o valor de um input, ou alguma outra forma de o usuário inserir infromações

        excel_header = ['Matricula', 'Nome','Senha','Time','Cargo'] # Aqui estamos informando os nomes das colunas
        cadastro_df = pd.DataFrame(data = pd.read_excel('arquivo.xlsx', engine='openpyxl'), columns=excel_header) # Aqui estamos criando um DataFrame com as informações do arquivo excel

        if window == matricula and eventos == sg.WINDOW_CLOSED: # Aqui estamos especificando o que será feito quando clicar no X da janela sendo "sg.WINDOW_CLOSE" o evento
            break # Este comando serve para encerrar uma repetição

        if window == matricula and eventos in ['-CONFIRMAR-']: # Aqui estamos especificando o que será feito quando clicar no botão 'Confirmar'
            if valores['-MATRICULA-'] and valores['-NOME-'] and valores['-SENHA-'] and valores['-TIME-'] and valores['-CARGO-'] != '': # Aqui estamos verificando se todos os campos estão preenchidos
                l = cadastro_df['Matricula'].count() # Aqui estamos contando o número de linhas na coluna 'Matrícula'
                cadastro_df.loc[l+1] = ([valores['-MATRICULA-']] + [valores['-NOME-']] + [valores['-SENHA-']] + [valores['-TIME-']] + [valores['-CARGO-']]) # Aqui estamos adicionando mais uma linha no dataframe com as informações fornecidas pelo usuário
                writer = pd.ExcelWriter('arquivo.xlsx') # Aqui estamos criando a variávle responsavel por gravar as informações no arquivo excel
                cadastro_df.to_excel(writer) # Aqui estamos dando o comando de escrever
                writer.save() # Aqui estamos dando o comando de salvar o arquivo
                matricula.close() # Aqui estamos dando o comando de encerrar a janela
                matricula = fun_matricula() # Aqui estamos dando o comando de executar novamente a janela para que a mesma fique limpa
                sg.popup_quick("Cadastrado com sucesso!") # Aqui estamos retornando um aviso ao usuário
            else: # Aqui estamos especificando o que irá ocorrer se o que o 'IF' pedir não for atendido
                sg.popup_quick("Necessario preencher todos os campos!") # Aqui estamos retornando um aviso ao usuário

First() # Este comando serve para que a classe seja executada