import csv
import os

# Diretório onde os arquivos CSV estão localizados
diretorio = r'C:\Users\PMH\Documents\Franklin\cadastro_postos\SISREG'

# Nome do arquivo resultante
arquivo_resultante = 'sisreg.csv'

# Lista para armazenar dados de todos os arquivos CSV
dados_totais = []

# Loop pelos arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.csv'):
        caminho_completo = os.path.join(diretorio, nome_arquivo)
        with open(caminho_completo, 'r', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=';')  # Use ponto e vírgula como separador
            # Ignora o cabeçalho nos arquivos subsequentes (a partir do segundo)
            if dados_totais:
                next(leitor_csv)
            # Adiciona os dados à lista total
            dados_totais.extend(leitor_csv)

# Escreve os dados totais no arquivo resultante
with open(arquivo_resultante, 'w', newline='') as arquivo_resultante_csv:
    escritor_csv = csv.writer(arquivo_resultante_csv, delimiter=';')  # Use ponto e vírgula como separador
    # Cabeçalho, se necessário
    # escritor_csv.writerow(["Coluna1", "Coluna2", ...])
    escritor_csv.writerows(dados_totais)
