import pandas as pd
import csv
import pyautogui

arquivo = 'chaves.csv'
df = pd.read_csv(arquivo)

# Convert 'solicitacao' column to strings for consistent data types
solicitacao_arquivo = set(map(str, df['solicitacao']))

while True:
    solicitacao = pyautogui.prompt(text='Digite a SOLICITAÇÃO:', title='Exames')
    
    if solicitacao in solicitacao_arquivo:
        print('Já adicionado')
    else:
        chave = pyautogui.prompt(text='Digite a CHAVE:', title='Exames')

        with open('chaves.csv', 'a', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow([solicitacao, chave])

        # Update the set to include the new 'solicitacao'
        solicitacao_arquivo.add(solicitacao)
