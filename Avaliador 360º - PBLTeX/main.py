import PySimpleGUI as sg
import pandas as pd

sg.theme('LightGreen1')
sg.set_options(font=('Arial', 20))

nivel = 0 # 1 = adm, 2 = professor, 3 = aluno

times =[]
nome =[]
select = []

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
        sg.pin(sg.Button('Avaliar Alunos', size=(13, 1), key='-AVALIAR-')),
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
    global times, nome, select

    nome_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'))

    l=0
    for i in nome_df.itertuples():
        time = nome_df.iat[l,4]
        if time != 'Admin' and time != 'Professor' and time not in times:
            times.append(time)
        l+=1

    times.sort()
    nome.sort()

    esquerda = [
        [sg.Text('Time:')],
        [sg.Text('Aluno:')],
        [sg.Text('Matrícula:')],
        [sg.Text('Senha:')],
        [sg.Text('Time:', size=(10))],
        [sg.Text('Cargo:', size=(10))],
    ]

    direita = [
        [sg.Combo(times, expand_x=True, size=(20, 5), readonly=True, enable_events=True, key='-SELECT_T-')],
        [sg.Combo(nome, expand_x=True, size=(20, 5), readonly=True, enable_events=True, key='-SELECT_C1-')],
        [sg.Input(key='-MATRICULA-', readonly=True)],
        [sg.Input(password_char='*', key='-SENHA-')],
        [sg.Input(size=(10), key='-TIME-')],
        [sg.Input(readonly=True, size=(10), key='-CARGO-')],
    ]

    layout_consultar = [
        [sg.Text('Alunos', expand_x=True, justification='center')],
        [sg.Column(esquerda),sg.Column(direita)],
        [sg.Button('Alterar', expand_x=True, key='-ALTERAR-')],
        [sg.Button('Retornar', expand_x=True, key='-BACK-')],

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
        [sg.Text('1. Trabalho em equipe, cooperação e descentralização de conhecimento')],
        [sg.Combo(notas, size=(3, 1), readonly=True, key='-M1-',)],
        [sg.Text('2. Iniciativa e proatividade')],
        [sg.Combo(notas, size=(3, 1), readonly=True, key='-M2-')],
        [sg.Text('3. Autodidaxia e agregação de conhecimento ao grupo')],
        [sg.Combo(notas, size=(3, 1), readonly=True, key='-M3-')],
        [sg.Text('4. Entrega de resultados e participação efetiva no projeto')],
        [sg.Combo(notas, size=(3, 1), readonly=True, key='-M4-')],
        [sg.Text('5. Competência técnica')],
        [sg.Combo(notas, size=(3, 1), readonly=True, key='-M5-')],
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
    global nivel, times, nome, select
    nome_cons = []
    nome_df = pd.DataFrame(data = pd.read_excel('Avaliador 360º - PBLTeX/arquivo.xlsx', engine='openpyxl'))

    l=0
    for i in nome_df.itertuples():
        time = nome_df.iat[l,4]
        if time != 'Admin' and time != 'Professor' and time not in times:
            times.append(time)
        l+=1

    times.sort()
    nome.sort()

    for linha in nome_df['Nome']:
        nome_cons.append(linha)

    label=[
        [sg.Text('Time:')],
        [sg.Text('Aluno:')]
        ]

    vallabel=[
        [sg.Combo(times, expand_x=True, size=(20, 5), readonly=True, enable_events=True, key='-SELECT_T1-')],
        [sg.Combo(nome, expand_x=True, size=(20, 5), readonly=True, enable_events=True, key='-SELECT_C2-')]
        ]

    sklls = [
        [sg.Text('1. Trabalho em equipe, cooperação e descentralização de conhecimento')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM1-')],
        [sg.Text('2. Iniciativa e proatividade')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM2-')],
        [sg.Text('3. Autodidaxia e agregação de conhecimento ao grupo')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM3-')],
        [sg.Text('4. Entrega de resultados e participação efetiva no projeto')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM4-')],
        [sg.Text('5. Competência técnica')],
        [sg.Input(size=(5, 1), readonly=True, key='-INPM5-')]
    ]

    notas = [
        [sg.ProgressBar(5, orientation='h', size=(30, 30), border_width=1, key='-BARM1-')],
        [sg.Text('')],
        [sg.ProgressBar(5, orientation='h', size=(30, 30),  border_width=1, key='-BARM2-')],
        [sg.Text('')],
        [sg.ProgressBar(5, orientation='h', size=(30, 30), border_width=1, key='-BARM3-')],
        [sg.Text('')],
        [sg.ProgressBar(5, orientation='h', size=(30, 30), border_width=1, key='-BARM4-')],
        [sg.Text('')],
        [sg.ProgressBar(5, orientation='h', size=(30, 30), border_width=1, key='-BARM5-')],   
    ]
    if nivel == 2: # acessso nivel professor
        layout_ver_notas = [
            [sg.Text('Alunos', expand_x=True, justification='center')],
            [sg.Combo(nome_cons, expand_x=True, readonly=True, enable_events=True, key='-SELECT_N-')],
            [sg.Text('Matrícula'), sg.Input(key='-MATRICULA-', size=(7, 1), readonly=True)],
            [sg.Column(sklls),sg.Column(notas)],
            [sg.Button('Modificar', expand_x=True, key='MODIFICAR')], 
            [sg.Button('Retornar', expand_x=True, key='-BACK-')]
        ]
    else: # acessos de nivel adm e aluno
        layout_ver_notas = [
            [sg.Text('Alunos', expand_x=True, justification='center')],
            [sg.Column(label),sg.Column(vallabel, expand_x=True)],
            [sg.Text('Matrícula'), sg.Input(key='-MATRICULA-', size=(7, 1), readonly=True)],
            [sg.Column(sklls),sg.Column(notas)],    
            [sg.Button('Retornar', expand_x=True, key='-BACK-')]
        ]
    return sg.Window('Consultar', layout=layout_ver_notas, margins=(10, 10), finalize=True)

tela, login = fun_login(), None

val1 = 0

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
                        sg.popup_ok("Aluno Avaliado Com Sucesso!")
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
                sg.popup_ok("Aluno Avaliado Com Sucesso!")
            x += 1

    if eventos in ['-SELECT_T-']:       # filtro por times
        if val1 != 0:
            select.clear()
            val1+=1
        select.clear()
        times.clear()
        nome.clear()
        select.append(valores['-SELECT_T-'])
        x = 0
        for i in df.itertuples():
            if df.iat[x,3] in select:       # validacao dos nomes
                nome.append(df.at[x,'Nome'])   
            x+=1
        tela.close()
        tela = fun_consultar()
        tela['-SELECT_T-'].update('')
        val = select[0]
        tela['-SELECT_T-'].update(val)
        print(select)
        print(nome)
        
    if eventos in ['-SELECT_T1-']:       # filtro por times
        if val1 != 0:
            select.clear()
            val1+=1
        select.clear()
        times.clear()
        nome.clear()
        select.append(valores['-SELECT_T1-'])
        x = 0
        for i in df.itertuples():
            if df.iat[x,3] in select:       # validacao dos nomes
                nome.append(df.at[x,'Nome'])   
            x+=1
        tela.close()
        tela = fun_see_notas()
        tela['-SELECT_T1-'].update('')
        val = select[0]
        tela['-SELECT_T1-'].update(val)
        print(select)
        print(nome)

    if eventos in ['-SELECT_C1-']:
        print(valores['-SELECT_C1-'])
        x=0
        for i in df.itertuples():
            if df.iat[x,1] == valores['-SELECT_C1-']:
                tela['-MATRICULA-'].update(df.iat[x,0])
                tela['-SENHA-'].update(df.iat[x,2])
                tela['-TIME-'].update(df.iat[x,3])
                tela['-CARGO-'].update(df.iat[x,4])
                break
            x+=1

    if eventos in ['-SELECT_C2-']:

        linha = 0
        for i in df.itertuples():
            if df.iat[linha,1] == valores['-SELECT_C2-']:
                break
            linha += 1

        pessoas =[]
        for i in df.itertuples():
            i=list(i)
            if i[4] == df.iat[linha,3]:
                pessoas.append(i[4])

        n1 = float(df.at[linha,'m1']/len(pessoas))
        n2 = float(df.at[linha,'m2']/len(pessoas))
        n3 = float(df.at[linha,'m3']/len(pessoas))
        n4 = float(df.at[linha,'m4']/len(pessoas))
        n5 = float(df.at[linha,'m5']/len(pessoas))

        janela['-MATRICULA-'].update(df.iat[linha,0])        

        janela['-BARM1-'].update(n1)
        janela['-BARM2-'].update(n2)
        janela['-BARM3-'].update(n3)
        janela['-BARM4-'].update(n4)
        janela['-BARM5-'].update(n5)

        janela['-INPM1-'].update(n1)
        janela['-INPM2-'].update(n2)
        janela['-INPM3-'].update(n3)
        janela['-INPM4-'].update(n4)
        janela['-INPM5-'].update(n5)

    if eventos in ['-ALTERAR-']:
        if valores['-SELECT_C1-'] == '':
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

                nome_time = (df.at[x, 'Time'])
                ##time_todos = df['Time']
                time_integrantes_quantidade = 0
                for time_verificador in df['Time']:
                    if time_verificador == nome_time:
                        time_integrantes_quantidade += 1
                print(nome_time, time_integrantes_quantidade)
                if str(df.loc[x].at['m1']) and str(df.loc[x].at['m2']) and str(df.loc[x].at['m3']) \
                     and str(df.loc[x].at['m4']) and str(df.loc[x].at['m5']) == 'nan':
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
                    sg.popup_ok('Usuário sem notas para consultar')
                    break
                else:
                    p_m1 = float(df.loc[x].at['m1']/time_integrantes_quantidade)
                    p_m2 = float(df.loc[x].at['m2']/time_integrantes_quantidade)
                    p_m3 = float(df.loc[x].at['m3']/time_integrantes_quantidade)
                    p_m4 = float(df.loc[x].at['m4']/time_integrantes_quantidade)
                    p_m5 = float(df.loc[x].at['m5']/time_integrantes_quantidade)

                    janela['-MATRICULA-'].update(value=df.loc[x].at['Matricula'])
                    if p_m1 <= 2:
                        janela['-BARM1-'].update(p_m1, bar_color=('red', 'white'))
                    if p_m1 > 2 and p_m1 < 4:
                        janela['-BARM1-'].update(p_m1, bar_color=('yellow', 'white'))
                    if p_m1 >= 4:
                        janela['-BARM1-'].update(p_m1, bar_color=('green', 'white'))

                    if p_m2 <= 5:
                        janela['-BARM2-'].update(p_m2, bar_color=('red', 'white'))
                    if p_m2 > 2 and p_m2 < 4:
                        janela['-BARM2-'].update(p_m2, bar_color=('yellow', 'white'))
                    if p_m2 >= 4:
                        janela['-BARM2-'].update(p_m2, bar_color=('green', 'white'))

                    if p_m3 <= 2:
                        janela['-BARM3-'].update(p_m3, bar_color=('red', 'white'))
                    if p_m3 > 2 and p_m3 < 4:
                        janela['-BARM3-'].update(p_m3, bar_color=('yellow', 'white'))
                    if p_m3 >= 4:
                        janela['-BARM3-'].update(p_m3, bar_color=('green', 'white'))

                    if p_m4 <= 2:
                        janela['-BARM4-'].update(p_m4, bar_color=('red', 'white'))
                    if p_m4 > 2 and p_m4 < 4:
                        janela['-BARM4-'].update(p_m4, bar_color=('yellow', 'white'))
                    if p_m4 >= 4:
                        janela['-BARM4-'].update(p_m4, bar_color=('green', 'white'))

                    if p_m5 <= 2:
                        janela['-BARM5-'].update(p_m5, bar_color=('red', 'white'))
                    if p_m5 > 2 and p_m5 < 4:
                        janela['-BARM5-'].update(p_m5, bar_color=('yellow', 'white'))
                    if p_m5 >= 4:
                        janela['-BARM5-'].update(p_m5, bar_color=('green', 'white'))

                    janela['-INPM1-'].update(float(df.loc[x].at['m1']/time_integrantes_quantidade))
                    janela['-INPM2-'].update(float(df.loc[x].at['m2']/time_integrantes_quantidade))
                    janela['-INPM3-'].update(float(df.loc[x].at['m3']/time_integrantes_quantidade))
                    janela['-INPM4-'].update(float(df.loc[x].at['m4']/time_integrantes_quantidade))
                    janela['-INPM5-'].update(float(df.loc[x].at['m5']/time_integrantes_quantidade))
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