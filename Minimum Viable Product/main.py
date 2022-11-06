import PySimpleGUI as sg
import pandas as pd

sg.theme('LightGreen1')
sg.set_options(font=('Arial', 20))

nivel = 0 # 1 = adm, 2 = professor, 3 = aluno

def fun_login():
    layout_login = [
        [sg.Text('Usuário')], [sg.Input(key='usuário', size=(30,30))],
        [sg.Text('Senha')], [sg.Input(key='senha', password_char= '*', size=(25,30)), sg.Checkbox('Ver', enable_events=True, key='-VER_L-')],
        [sg.Button('Entrar', key='-ENTRAR-')],
    ]
    return sg.Window('Login', layout=layout_login, margins=(10,10),finalize=True)
    
def fun_aluno():
    global nivel
    nivel = 3
    layout_aluno = [
        [sg.Text('Logado como aluno', expand_x=True, justification='center', key='-NOME_USUARIO-')],
        [sg.pin(sg.Button('Avaliar colegas', size=(13, 1), key='-AVALIAR-')),
        sg.pin(sg.Button('Consultar notas', size=(13, 1), key='-NOTAS-')),],
        [sg.pin(sg.Button('Deslogar', size=(27, 1), key='-DESLOGAR-'))],
    ]
    return sg.Window('Aluno', layout=layout_aluno, margins=(10, 10), finalize=True)

def fun_professor():
    global nivel
    nivel = 2
    layout_professor = [
        [sg.Text('Logado como professor', expand_x=True, justification='center', key='-NOME_USUARIO-')],
        [sg.pin(sg.Button('Consultar alunos', size=(13, 1), key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', size=(13, 1), key='-TIMES-')),
        sg.pin(sg.Button('Consultar notas', size=(13, 1), key='-NOTAS-')),],
        [sg.pin(sg.Button('Deslogar', size=(41, 1), key='-DESLOGAR-'))],
    ]
    return sg.Window('Professor', layout=layout_professor, margins=(10, 10), finalize=True)

def fun_adm():
    global nivel
    nivel = 1
    layout_adm = [
        [sg.Text('Logado como administrador', expand_x=True, justification='center', key='-NOME_USUARIO-')],
        [sg.pin(sg.Button('Consultar alunos', size=(13, 1), key='-ALUNOS-')),
        sg.pin(sg.Button('Consultar times', size=(13, 1), key='-TIMES-')),
        sg.pin(sg.Button('Consultar notas', size=(13, 1), key='-NOTAS-')),],
        [sg.pin(sg.Button('Cadastrar', size=(20, 1), key='-CADASTRO-')),
        sg.pin(sg.Button('Deslogar', size=(20, 1), key='-DESLOGAR-'))],
    ]
    return sg.Window('Administrador', layout=layout_adm, margins=(10, 10), finalize=True)

def fun_consultar():

    nome = []
    nome_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'))

    for linha in nome_df['Nome']:
        nome.append(linha)
    
    layout_consultar = [
        [sg.Text('Alunos', expand_x=True, justification='center')],
        [sg.Combo(nome, expand_x=True, size=(20, 5), readonly=True, enable_events=True, key='-SELECT_C-')],
        [sg.Text('Matrícula'), sg.Input(key='-MATRICULA-', readonly=True)],
        [sg.Text('Nome'), sg.Input(key='-NOME-')],
        [sg.Text('Senha'), sg.Input(password_char='*', key='-SENHA-')],
        [sg.Text('Time', size=(10)), sg.Input(size=(10), key='-TIME-'),
        sg.Text('Cargo', size=(10)), sg.Combo(['Aluno', 'PO', 'SM', 'Professor', 'Admin'], readonly=True, size=(10), key='-CARGO-')],
        [sg.Button('Alterar', expand_x=True, key='-ALTERAR-'),
        sg.Button('Retornar', expand_x=True, key='-BACK-')],
    ]
    return sg.Window('Consultar', layout=layout_consultar, margins=(10, 10), finalize=True)

def fun_times():
    times_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'))
    times = []

    for list in times_df['Time']:
        if list not in times:
            times.append(list)

    layout_times = [
        [sg.Listbox(times, size=(15, 5))],
        [sg.Button('Retornar', expand_x=True, key='-BACK-')]
    ]
    return sg.Window('Times', layout=layout_times, margins=(10, 10), finalize=True)

def fun_avaliar():
    nome = []
    notas = [1, 2, 3, 4, 5]
    nome_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'))

    for linha in nome_df['Nome']:
        nome.append(linha)
    
    layout_avaliar = [
        [sg.Text('Alunos', expand_x=True, justification='center')],
        [sg.Combo(nome, expand_x=True, readonly=True, enable_events=True, key='-SELECT_A-')],
        [sg.Text('Matrícula'), sg.Input(key='-MATRICULA-', size=(7, 1), readonly=True)],
        [sg.Text('Matéria 1', size=(10, 1)),sg.Combo(notas, size=(3, 1), readonly=True, key='-M1-')],
        [sg.Text('Matéria 2', size=(10, 1)),sg.Combo(notas, size=(3, 1), readonly=True, key='-M2-')],
        [sg.Text('Matéria 3', size=(10, 1)),sg.Combo(notas, size=(3, 1), readonly=True, key='-M3-')],
        [sg.Text('Matéria 4', size=(10, 1)),sg.Combo(notas, size=(3, 1), readonly=True, key='-M4-')],
        [sg.Text('Matéria 5', size=(10, 1)),sg.Combo(notas, size=(3, 1), readonly=True, key='-M5-')],
        [sg.Button('Salvar', expand_x=True, key='-ENVIAR-'),
        sg.Button('Retornar', expand_x=True, key='-BACK-')],
    ]
    return sg.Window('Avaliar', layout=layout_avaliar, margins=(10, 10), finalize=True)

def fun_cadastrar():
    Cargo = [
        [sg.Text('Cargo', size=(10)), sg.Combo(['Aluno', 'PO', 'SM', 'Professor', 'Admin'], readonly=True, size=(10), expand_x=True, key='-CARGO-')]
    ]
    Time = [
        [sg.Text('Time', size=(10)), sg.Input(size=(10), expand_x=True, key='-TIME-')]
    ]
    layout_cadastrar = [
        [sg.Text('Matrícula'), sg.Input(expand_x=True, key='-MATRICULA-')],
        [sg.Text('Nome'), sg.Input(expand_x=True, key='-NOME-')],
        [sg.Text('Senha'), sg.Input(expand_x=True, key='-SENHA-')],
        [sg.Column(Cargo),sg.Column(Time)],
        [sg.Button('Cadastrar', expand_x=True, key='-CADASTRAR-')],
        [sg.Button('Retornar', expand_x=True, key='-BACK-')]
    ]
    return sg.Window('Cadastrar', layout=layout_cadastrar, margins=(10, 10), finalize=True)

def fun_see_notas():
    global nivel
    nome = []
    nome_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'))

    for linha in nome_df['Nome']:
        nome.append(linha)

    sklls = [
        [sg.Text('1. Trabalho Em Equipe, Cooperação E Descentralização De Conhecimento')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM1-')],
        [sg.Text('2. Iniciativa e proatividade')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM2-')],
        [sg.Text('3. Autodidaxia E Agregação De Conhecimento Ao Grupo')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM3-')],
        [sg.Text('4. Entrega de Resultados E Participação Efetiva No Projeto')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM4-')],
        [sg.Text('5. Competência Técnica')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM5-')]
    ]

    notas = [
        [sg.ProgressBar(50, orientation='h', size=(30, 30), border_width=1, key='-BARM1-')],
        [sg.Text('')],
        [sg.ProgressBar(50, orientation='h', size=(30, 30),  border_width=1, key='-BARM2-')],
        [sg.Text('')],
        [sg.ProgressBar(50, orientation='h', size=(30, 30), border_width=1, key='-BARM3-')],
        [sg.Text('')],
        [sg.ProgressBar(50, orientation='h', size=(30, 30), border_width=1, key='-BARM4-')],
        [sg.Text('')],
        [sg.ProgressBar(50, orientation='h', size=(30, 30), border_width=1, key='-BARM5-')],   
    ]
    if nivel == 2: # acessso nivel professor
        layout_ver_notas = [
            [sg.Text('Alunos', expand_x=True, justification='center')],
            [sg.Combo(nome, expand_x=True, readonly=True, enable_events=True, key='-SELECT_N-')],
            [sg.Text('Matrícula'), sg.Input(key='-MATRICULA-', size=(7, 1), readonly=True)],
            [sg.Column(sklls),sg.Column(notas)],
            [sg.Button('Modificar', expand_x=True, key='MODIFICAR')], 
            [sg.Button('Retornar', expand_x=True, key='-BACK-')]
        ]
    else: # acessos de nivel adm e aluno
        layout_ver_notas = [
            [sg.Text('Alunos', expand_x=True, justification='center')],
            [sg.Combo(nome, expand_x=True, readonly=True, enable_events=True, key='-SELECT_N-')],
            [sg.Text('Matrícula'), sg.Input(key='-MATRICULA-', size=(7, 1), readonly=True)],
            [sg.Column(sklls),sg.Column(notas)],
            [sg.Button('Retornar', expand_x=True, key='-BACK-')]
        ]
    return sg.Window('Consultar', layout=layout_ver_notas, margins=(10, 10), finalize=True)

tela, login = fun_login(), None

while True:
    janela, eventos, valores = sg.read_all_windows()

    excel_header = ['Matricula', 'Nome','Senha','Time','Cargo', 'm1', 'm2', 'm3', 'm4', 'm5']
    df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'), columns=excel_header)

    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos in ['-VER_L-']:
        if valores['-VER_L-'] == True:
            janela['senha'].update(password_char='')
        if valores['-VER_L-'] == False:
            janela['senha'].update(password_char='*')

    if eventos in ['-ENTRAR-']:

        login = df['Matricula']
        senha = df['Senha']
        cargo = df['Cargo']

        if valores ['usuário'] == '' or valores ['senha'] == '':
            sg.popup_ok("Preencha Todos os campos")
        else:
            x = 0
            for usuario in login:
                if valores['usuário'] == str(usuario):
                    if valores['senha'] == str(senha[x]):
                        tela.close()
                        if str(cargo[x]) == 'Aluno' or str(cargo[x]) == 'PO' or str(cargo[x]) ==  'SM':
                            login = fun_aluno()
                        if str(cargo[x]) == 'Professor':
                            login = fun_professor()
                        if str(cargo[x]) == 'Admin':
                            login = fun_adm()
                        x = 0
                        break
                x += 1
            if x > 0:
                sg.popup_ok("Verifique seu login ou senha.")
    
    if eventos in ['-AVALIAR-']:
        login.hide()
        tela = fun_avaliar()

    if eventos in ['-SELECT_A-']:
        x = 0
        for linha in df['Nome']:
            if linha == valores['-SELECT_A-']:
                janela['-MATRICULA-'].update(value=df.loc[x].at['Matricula'])
                janela['-M1-'].update('   ')
                janela['-M2-'].update('   ')
                janela['-M3-'].update('   ')
                janela['-M4-'].update('   ')
                janela['-M5-'].update('   ')

            x += 1
    
    if eventos in ['-ENVIAR-']:
        if valores['-SELECT_A-'] == '':
            sg.popup_ok('Selecione um colega para ser avaliado')
        if valores['-M1-'] and valores['-M2-'] and valores['-M3-'] and valores['-M4-'] and valores['-M5-'] != '   ':
            x = 0
            for linha in df['Matricula']:
                if valores['-MATRICULA-'] == str(linha):
                    if str(df.at[x, 'm1']) and str(df.at[x, 'm2']) and str(df.at[x, 'm3']) and str(df.at[x, 'm4']) and str(df.at[x, 'm5']) != 'nan':
                        df.at[x, 'm1'] = int(df.at[x, 'm1']) + int(valores['-M1-'])
                        df.at[x, 'm2'] = int(df.at[x, 'm2']) + int(valores['-M2-'])
                        df.at[x, 'm3'] = int(df.at[x, 'm3']) + int(valores['-M3-'])
                        df.at[x, 'm4'] = int(df.at[x, 'm4']) + int(valores['-M4-'])
                        df.at[x, 'm5'] = int(df.at[x, 'm5']) + int(valores['-M5-'])
                        janela['-M1-'].update('   ')
                        janela['-M2-'].update('   ')
                        janela['-M3-'].update('   ')
                        janela['-M4-'].update('   ')
                        janela['-M5-'].update('   ')
                    else:
                        df.at[x, 'm1'] = int(valores['-M1-'])
                        df.at[x, 'm2'] = int(valores['-M2-'])
                        df.at[x, 'm3'] = int(valores['-M3-'])
                        df.at[x, 'm4'] = int(valores['-M4-'])
                        df.at[x, 'm5'] = int(valores['-M5-'])
                        janela['-M1-'].update('   ')
                        janela['-M2-'].update('   ')
                        janela['-M3-'].update('   ')
                        janela['-M4-'].update('   ')
                        janela['-M5-'].update('   ')
                    writer = pd.ExcelWriter('Avaliador 360º - PBLTeX/arquivo.xlsx')
                    df.to_excel(writer)
                    writer.save()
                x += 1
        else:
            sg.popup_ok('Informe todas as notas')

    if eventos in ['-ALUNOS-']:
        login.hide()
        tela = fun_consultar()
    
    if eventos in ['-SELECT_C-']:
        x = 0
        for linha in df['Nome']:
            if linha == valores['-SELECT_C-']:
                janela['-MATRICULA-'].update(value=df.loc[x].at['Matricula'])
                janela['-NOME-'].update(value=df.loc[x].at['Nome'])
                janela['-SENHA-'].update(value=df.loc[x].at['Senha'])
                janela['-TIME-'].update(value=df.loc[x].at['Time'])
                janela['-CARGO-'].update(value=df.loc[x].at['Cargo'])
            x += 1
    
    if eventos in ['-ALTERAR-']:
        if valores['-SELECT_C-'] == '':
            sg.popup_ok('Selecione o usuário para ser alterado')
        elif valores['-NOME-'] and valores['-SENHA-'] and valores['-TIME-'] and valores['-CARGO-'] != '':
            x = 0
            for linha in df['Matricula']:
                if valores['-MATRICULA-'] == str(linha):
                    df.at[x, 'Nome'] =  valores['-NOME-']
                    df.at[x, 'Senha'] = valores['-SENHA-']
                    df.at[x, 'Time'] = valores['-TIME-']
                    df.at[x, 'Cargo'] = valores['-CARGO-']
                    writer = pd.ExcelWriter('Avaliador 360º - PBLTeX/arquivo.xlsx')
                    df.to_excel(writer)
                    writer.save()                        
                    janela['-MATRICULA-'].update('')
                    janela['-NOME-'].update('')
                    janela['-SENHA-'].update('')
                    janela['-TIME-'].update('')
                    janela['-CARGO-'].update('')
                x += 1
        else:
            sg.popup_ok('Preencha todos os campos')
    if eventos in ['-TIMES-']:
        login.hide()
        tela = fun_times()

    if eventos in ['-NOTAS-']:
        login.hide()
        tela = fun_see_notas()

    if eventos in ['-SELECT_N-']:
        x = 0
        for linha in df['Nome']:
            if linha == valores['-SELECT_N-']:
                if str(df.loc[x].at['m1']) and str(df.loc[x].at['m2']) and str(df.loc[x].at['m3']) and str(df.loc[x].at['m4']) and str(df.loc[x].at['m5']) == 'nan':
                    sg.popup_ok('Usuário sem notas para consultar')
                    janela['-MATRICULA-'].update(value=df.loc[x].at['Matricula'])
                    janela['-BARM1-'].update(0)
                    janela['-BARM2-'].update(0)
                    janela['-BARM3-'].update(0)
                    janela['-BARM4-'].update(0)
                    janela['-BARM5-'].update(0)

                    janela['-INPM1-'].update('')
                    janela['-INPM2-'].update('')
                    janela['-INPM3-'].update('')
                    janela['-INPM4-'].update('')
                    janela['-INPM5-'].update('')
                    break
                else:
                    p_m1 = int(df.loc[x].at['m1'])
                    p_m2 = int(df.loc[x].at['m2'])
                    p_m3 = int(df.loc[x].at['m3'])
                    p_m4 = int(df.loc[x].at['m4'])
                    p_m5 = int(df.loc[x].at['m5'])

                    janela['-MATRICULA-'].update(value=df.loc[x].at['Matricula'])
                    if p_m1 <= 25:
                        janela['-BARM1-'].update(p_m1, bar_color=('red', 'white'))
                    if p_m1 > 25 and p_m1 < 40:
                        janela['-BARM1-'].update(p_m1, bar_color=('yellow', 'white'))
                    if p_m1 >= 40:
                        janela['-BARM1-'].update(p_m1, bar_color=('green', 'white'))

                    if p_m2 <= 25:
                        janela['-BARM2-'].update(p_m2, bar_color=('red', 'white'))
                    if p_m2 > 25 and p_m2 < 40:
                        janela['-BARM2-'].update(p_m2, bar_color=('yellow', 'white'))
                    if p_m2 >= 40:
                        janela['-BARM2-'].update(p_m2, bar_color=('green', 'white'))

                    if p_m3 <= 25:
                        janela['-BARM3-'].update(p_m3, bar_color=('red', 'white'))
                    if p_m3 > 25 and p_m3 < 40:
                        janela['-BARM3-'].update(p_m3, bar_color=('yellow', 'white'))
                    if p_m3 >= 40:
                        janela['-BARM3-'].update(p_m3, bar_color=('green', 'white'))

                    if p_m4 <= 25:
                        janela['-BARM4-'].update(p_m4, bar_color=('red', 'white'))
                    if p_m4 > 25 and p_m4 < 40:
                        janela['-BARM4-'].update(p_m4, bar_color=('yellow', 'white'))
                    if p_m4 >= 40:
                        janela['-BARM4-'].update(p_m4, bar_color=('green', 'white'))

                    if p_m5 <= 25:
                        janela['-BARM5-'].update(p_m5, bar_color=('red', 'white'))
                    if p_m5 > 25 and p_m5 < 40:
                        janela['-BARM5-'].update(p_m5, bar_color=('yellow', 'white'))
                    if p_m5 >= 40:
                        janela['-BARM5-'].update(p_m5, bar_color=('green', 'white'))

                    janela['-INPM1-'].update(int(df.loc[x].at['m1']))
                    janela['-INPM2-'].update(int(df.loc[x].at['m2']))
                    janela['-INPM3-'].update(int(df.loc[x].at['m3']))
                    janela['-INPM4-'].update(int(df.loc[x].at['m4']))
                    janela['-INPM5-'].update(int(df.loc[x].at['m5']))
            x += 1

    if eventos in ['-CADASTRO-']:
        login.hide()
        tela = fun_cadastrar()
    
    if eventos in ['-CADASTRAR-']:
        if valores['-MATRICULA-'] and valores['-NOME-'] and valores['-SENHA-'] and valores['-TIME-'] and valores['-CARGO-'] != '':
            salvar = True
            for ver in df['Matricula']:
                if valores['-MATRICULA-'] == str(ver):
                    salvar = False
                    break
            if salvar == True:
                df = pd.concat([df, pd.DataFrame({'Matricula':[valores['-MATRICULA-']], 'Nome': [valores['-NOME-']], 'Senha':[valores['-SENHA-']], 'Time':[valores['-TIME-']], 'Cargo': [valores['-CARGO-']]})])
                writer = pd.ExcelWriter('Avaliador 360º - PBLTeX/arquivo.xlsx')
                df.to_excel(writer)
                writer.save()
                janela['-MATRICULA-'].update('')
                janela['-NOME-'].update('')
                janela['-SENHA-'].update('')
                janela['-TIME-'].update('')
                janela['-CARGO-'].update('')
                sg.popup_ok("Cadastrado com sucesso!")
            else:
                sg.popup_ok("Matricula já cadastrada")
        else:
            sg.popup_ok("É necessario preencher todos os campos!")

    if eventos in ['-BACK-']:
        tela.close()
        login.un_hide()

    if eventos in ['-DESLOGAR-']:
        login.close()
        tela = fun_login()
