import PySimpleGUI as sg

sg.theme('LightGreen1')
layout = [
    [sg.Text('Usuário',font=('Arial', 20)), sg.Input(font=('Arial', 20), key='usuário', size=(30,30))],
    [sg.Text('Senha',font=('Arial', 20)), sg.Input(font=('Arial', 20),key='senha', password_char= '*', size=(30,30))],
    [sg.Checkbox('Salvar Login',font=('Arial', 20))],
    [sg.Button('Entrar',font=('Arial', 20))]
]

janela = sg.Window('Tela de Login', layout=layout, margins=(20,20),finalize=True)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuário'] == 'excel' and valores ['senha'] == 'excel':
            sg.popup_quick("Bem Vindo")
        elif valores ['usuário'] == '' or valores ['senha'] == '':
            sg.popup_quick("Preencha Todos os campos")
        else:
            sg.popup_quick("Sua senha está errada")
