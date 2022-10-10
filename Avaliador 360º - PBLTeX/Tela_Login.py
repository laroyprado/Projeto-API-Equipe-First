import PySimpleGUI as sg
import pandas as pd

sg.theme('LightGreen1')
layout = [
    [sg.Text('Usuário',font=('Arial', 15))], [sg.Input(font=('Arial', 15), key='usuário', size=(30,30))],
    [sg.Text('Senha',font=('Arial', 15))], [sg.Input(font=('Arial', 15),key='senha', password_char= '*', size=(30,30))],
    [sg.Button('Entrar',font=('Arial', 15))]
]

janela = sg.Window('Tela de Login', layout=layout, margins=(20,20),finalize=True)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        
        df = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx')
        df.head()
                
        login = df['Matricula']
        senha = df['Senha']
         
           
    if valores ['usuário'] == '' or valores ['senha'] == '':
        sg.popup_quick("Preencha Todos os campos")
    else:
        x = 0
        for usuario in login:
            if valores['usuário'] == str(usuario):
                if valores['senha'] == str(senha[x]):
                    sg.popup_quick("Bem Vindo")
                    
                    x=0
                    break
                                
            x += 1                
        if x > 0:           
            sg.popup_quick("Verifique seu login ou senha.")
