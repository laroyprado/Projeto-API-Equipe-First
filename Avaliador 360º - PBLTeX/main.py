import PySimpleGUI as sg # Importação da ferramenta PySimpleGUI, após o comando "as" podemos definir o apelido "sg" para que seja mais rápido e facil usar a biblioteca
import pandas as pd #Importação da ferramenta Pandas, definindo o apelido "pd"
import numpy as np

sg.theme('LightGreen1') # Aqui definimos o tema que será usado no layout

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

def fun_adm():
    layout_adm = [
        [sg.Text('Bem vindo' , expand_x=True, justification='center', font=('Arial', 20))],
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

JanMatricula = fun_matricula() #aqui abrimmos a janela de matricula
JanADM, JanALUNOS, JanNOTAS, JanRANK = fun_adm(), None, None, None #aqui preparaos a abertura das telas de adm e suas subtelas. Serão abertas rodar 'JanXXX = funXXX()'


while True: # Este comando serve para iniciar uma repetição, para que o programa funcione continuamente
    window, eventos, valores = sg.read_all_windows()        
        # Este comando a cima serve para armazenar as informações de qual janela está aberta no momento, qual evento foi realizado e também qual valor foi inserido
        # window = serve para especificar a janela que está aberta no momento
        # eventos = serve para capturar alguma ação realizada na janela, como clicar em algum botão
        # valores = serve para receber o valor de um input, ou alguma outra forma de o usuário inserir infromações
        
    excel_header = ['Matricula', 'Nome','Senha','Time','Cargo'] # Aqui estamos informando os nomes das colunas
    cadastro_df = pd.DataFrame(data = pd.read_excel(r'C:\Users\danko\OneDrive\Documentos\GitHub\Projeto-API-Equipe-First\DataBase\arquivo.xlsx', engine='openpyxl'), columns=excel_header) # Aqui estamos criando um DataFrame com as informações do arquivo excel, mudar o endereco da pasta

    if eventos == sg.WINDOW_CLOSED: # Aqui estamos especificando o que será feito quando clicar no X da janela sendo "sg.WINDOW_CLOSE" o evento
        break # Este comando serve para encerrar uma repetição
    
    if window == JanMatricula and eventos in ['-CONFIRMAR-']: # Aqui estamos especificando o que será feito quando clicar no botão 'Confirmar'
        if valores['-MATRICULA-'] and valores['-NOME-'] and valores['-SENHA-'] and valores['-TIME-'] and valores['-CARGO-'] != '': # Aqui estamos verificando se todos os campos estão preenchidos
            salvar = True # Este parametro serve para verificar se o novo cadastro já pode ser salvo
            for ver in cadastro_df['Matricula']: # Aqui está sendo passado item por item da coluna 'Matricula' para a variavel 'ver'
                if valores['-MATRICULA-'] == str(ver): # Aqui estamos verificando se a matricula já existe
                    salvar = False # Caso exista o cadastro não deve ser salvo
                    break # Aqui estamos informando para parar o for caso encontre alguma matricula repetida
            if salvar == True: # Aqui estamos informando que se a variavel 'salvar' for igual a 'verdadeiro' (a matrícula não se repetir) o cadastro deve ser salvo no arquivo
                l = cadastro_df['Matricula'].count() # Aqui estamos contando o número de linhas na coluna 'Matrícula'
                cadastro_df.loc[l+1] = ([valores['-MATRICULA-']] + [valores['-NOME-']] + [valores['-SENHA-']] + [valores['-TIME-']] + [valores['-CARGO-']]) # Aqui estamos adicionando mais uma linha no dataframe com as informações fornecidas pelo usuário
                writer = pd.ExcelWriter(r'C:\Users\danko\OneDrive\Documentos\GitHub\Projeto-API-Equipe-First\DataBase\arquivo.xlsx') # Aqui estamos criando a variávle responsavel por gravar as informações no arquivo excel, mudar o endereco da pasta
                cadastro_df.to_excel(writer) # Aqui estamos dando o comando de escrever
                writer.save() # Aqui estamos dando o comando de salvar o arquivo
                JanMatricula.close() # Aqui estamos dando o comando de encerrar a janela
                JanMatricula = fun_matricula() # Aqui estamos dando o comando de executar novamente a janela para que a mesma fique limpa
                sg.popup_ok("Cadastrado com sucesso!") # Aqui estamos retornando um aviso ao usuário
            else:
                sg.popup_ok("Matricula já existente") # Aqui estamos retornando um aviso ao usuário
        else: # Aqui estamos especificando o que irá ocorrer se o que o 'IF' pedir não for atendido
            sg.popup_ok("Necessario preencher todos os campos!") # Aqui estamos retornando um aviso ao usuário

    #if teste_acesso == True:
    if eventos in ['-ALUNOS-']:# acessa tela alunos
        JanALUNOS = fun_adm_alunos()
        JanADM.hide()
    if eventos in ['-TIMES-']:#acessa tela times
        JanNOTAS = fun_adm_times()
        JanADM.hide()
    if eventos in ['-RANK-']:#acessa tela notas
        JanRANK = fun_adm_rank()
        JanADM.hide()
    if eventos in ['-ToADM-']:#volta para adm
        JanALUNOS.hide()
        JanADM.un_hide()
    if eventos in ['-ToADM-']:#volta para adm
        JanNOTAS.hide()
        JanADM.un_hide()
    if eventos in ['-ToADM-']:#volta para adm
        JanRANK.hide()
        JanADM.un_hide()

