import pandas as pd

editor_df = pd.read_excel('arquivo.xlsx')
editor_df.head()
print(editor_df)

linha = int(input('Qual Matrícula você deseja visualizar? '))
coluna = input('Qual informação você deseja visualizar? (Nome; Senha; Time; Cargo) ')

print(editor_df.loc[linha,coluna])