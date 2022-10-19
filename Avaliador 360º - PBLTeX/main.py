import PySimpleGUI as sg
import pandas as pd

sg.theme('LightGreen1')
sg.set_options(font=('Arial', 20))

class First():
    def fun_login():
        layout_login = [
            [sg.Text('Usuário')], [sg.Input(key='usuário', size=(30,30))],
            [sg.Text('Senha')], [sg.Input(key='senha', password_char= '*', size=(30,30))],
            [sg.Button('Entrar', key='-ENTRAR-')],
        ]
        return sg.Window('Tela de Login', layout=layout_login, margins=(10,10),finalize=True)
        
    def fun_aluno():
        None
    def fun_professor():
        None
    def fun_adm():
        layout_adm = [
            [sg.Text('Bem vindo', expand_x=True, justification='center')],
            [sg.pin(sg.Button('Consultar alunos', size=(13, 1), key='-ALUNOS-')),
            sg.pin(sg.Button('Consultar times', size=(13, 1), key='-TIMES-')),
            sg.pin(sg.Button('Consultar notas', size=(13, 1), key='-NOTAS-')),],
            [sg.pin(sg.Button('Cadastrar', size=(20, 1), key='-CADASTRO-')),
            sg.pin(sg.Button('Deslogar', size=(20, 1), key='-DESLOGAR-'))],
        ]
        return sg.Window('ADMINISTRADOR', layout=layout_adm, margins=(10, 10), finalize=True)

    def fun_consultar():

        nome = []
        nome_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'))

        for linha in nome_df['Nome']:
            nome.append(linha)
        
        layout_consultar = [
            [sg.Text('ALUNOS CADASTRADOS:', expand_x=True, justification='center')],
            [sg.Combo(nome, expand_x=True, size=(20, 5), key='-SELECT-')],
            [sg.Text('Matrícula'), sg.Input(key='-MATRICULA-', readonly=True)],
            [sg.Text('Nome'), sg.Input(key='-NOME-')],
            [sg.Text('Senha'), sg.Input(password_char='*', key='-SENHA-')],
            [sg.Text('Time', size=(10)), sg.Input(size=(10), key='-TIME-'),
            sg.Text('Cargo', size=(10)), sg.Combo(['Aluno', 'PO', 'SM', 'Professor', 'Admin'], enable_events=True, size=(10), key='-CARGO-')],
            [sg.Button('Consultar', expand_x=True, key='-CONSULTAR-'),
            sg.Button('Alterar', expand_x=True, key='-ALTERAR-'),
            sg.Button('Retornar', expand_x=True, key='-ToADM-')],
        ]
        return sg.Window('ALUNOS', layout=layout_consultar, margins=(10, 10), finalize=True)

    def fun_times():
        times_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'))
        times = []

        for list in times_df['Time']:
            if list not in times:
                times.append(list)

        layout_times = [
            [sg.Listbox(times, size=(15, 5))],
            [sg.Button('Retornar', expand_x=True, key='-ToADM-')]
        ]
        return sg.Window('TIMES', layout=layout_times, margins=(10, 10), finalize=True)
    def fun_avaliar():
        None
    def fun_notas():
        None
    def fun_cadastrar():
        layout_cadastrar = [
            [sg.Text('Matrícula'), sg.Input(key='-MATRICULA-')],
            [sg.Text('Nome'), sg.Input(key='-NOME-')],
            [sg.Text('Senha'), sg.Input(key='-SENHA-')],
            [sg.Text('Time', size=(10)), sg.Input(size=(10), key='-TIME-'),
            sg.Text('Cargo', size=(10)), sg.Combo(['Aluno', 'PO', 'SM', 'Professor', 'Admin'], enable_events=True, size=(10), key='-CARGO-')],
            [sg.Button('Cadastrar', expand_x=True, key='-CADASTRAR-'),
            sg.Button('Retornar', expand_x=True, key='-ToADM-')],
        ]
        return sg.Window('Cadastro', layout=layout_cadastrar, margins=(10, 10), finalize=True)

    tela = fun_login()

    while True:
        janela, eventos, valores = sg.read_all_windows()

        excel_header = ['Matricula', 'Nome','Senha','Time','Cargo']
        df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'), columns=excel_header)

        if eventos == sg.WINDOW_CLOSED:
            break

        if eventos in ['-ENTRAR-']:

            login = df['Matricula']
            senha = df['Senha']

            if valores ['usuário'] == '' or valores ['senha'] == '':
                sg.popup_ok("Preencha Todos os campos")
            else:
                x = 0
                for usuario in login:
                    if valores['usuário'] == str(usuario):
                        if valores['senha'] == str(senha[x]):
                            tela.close()
                            tela = fun_adm()
                            x=0
                            break                                        
                    x += 1                
                if x > 0:           
                    sg.popup_ok("Verifique seu login ou senha.")
        
        if eventos in ['-ALUNOS-']:
            tela.close()
            tela = fun_consultar()
        
        if eventos in ['-CONSULTAR-']:
            if valores['-SELECT-'] != '':
                x = 0
                for linha in df['Nome']:
                    if linha == valores['-SELECT-']:
                        janela['-MATRICULA-'].update(value=df.loc[x].at['Matricula'])
                        janela['-NOME-'].update(value=df.loc[x].at['Nome'])
                        janela['-SENHA-'].update(value=df.loc[x].at['Senha'])
                        janela['-TIME-'].update(value=df.loc[x].at['Time'])
                        janela['-CARGO-'].update(value=df.loc[x].at['Cargo'])
                    x += 1
            else:
                sg.popup_ok('Selecione um usuário')                
        
        if eventos in ['-ALTERAR-']:
            if valores['-SELECT-'] == '':
                sg.popup_ok('Selecione o usuário para ser alterado')
            elif valores['-NOME-'] and valores['-SENHA-'] and valores['-TIME-'] and valores['-CARGO-'] != '':
                x = 0
                for linha in df['Matricula']:
                    if valores['-MATRICULA-'] == str(linha):
                        df.at[x, 'Nome'] = valores['-NOME-']
                        df.at[x, 'Senha'] = valores['-SENHA-']
                        df.at[x, 'Time'] = valores['-TIME-']
                        df.at[x, 'Cargo'] = valores['-CARGO-']
                        writer = pd.ExcelWriter('Avaliador 360º - PBLTeX/arquivo.xlsx')
                        df.to_excel(writer)
                        writer.save()
                        tela.close()
                        tela = fun_consultar()
                    x += 1
            else:
                sg.popup_ok('Preencha todos os campos')

        if eventos in ['-TIMES-']:
            tela.close()
            tela = fun_times()

        if eventos in ['-NOTAS-']:
            None

        if eventos in ['-CADASTRO-']:
            tela.close()
            tela = fun_cadastrar()
        
        if eventos in ['-CADASTRAR-']:
            if valores['-MATRICULA-'] != int:
                sg.popup_ok("Matrícula inválida, é aceito somente números")
            else:
                if valores['-MATRICULA-'] and valores['-NOME-'] and valores['-SENHA-'] and valores['-TIME-'] and valores['-CARGO-'] != '':
                    salvar = True
                    for ver in df['Matricula']:
                        if valores['-MATRICULA-'] == str(ver):
                            salvar = False
                            break
                    if salvar == True:
                        l = df['Matricula'].count()
                        df.loc[l+1] = ([valores['-MATRICULA-']] + [valores['-NOME-']] + [valores['-SENHA-']] + [valores['-TIME-']] + [valores['-CARGO-']])
                        writer = pd.ExcelWriter('Avaliador 360º - PBLTeX/arquivo.xlsx')
                        df.to_excel(writer)
                        writer.save()
                        tela.close()
                        tela = fun_cadastrar()
                        sg.popup_ok("Cadastrado com sucesso!")
                    else:
                        sg.popup_ok("Matricula já cadastrada")
                else:
                    sg.popup_ok("É necessario preencher todos os campos!")

        if eventos in ['-ToADM-']:
            tela.close()
            tela = fun_adm()

        if eventos in ['-DESLOGAR-']:
            tela.close()
            tela = fun_login()
