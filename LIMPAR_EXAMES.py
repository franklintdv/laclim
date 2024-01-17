import pandas as pd

def remove_linhas_duplicadas(nome_arquivo):
    # Leitura do arquivo CSV com ';' como separador
    df = pd.read_csv(nome_arquivo, sep=';')

    # Remoção de linhas duplicadas
    df_sem_duplicatas = df.drop_duplicates()

    # Salva o novo DataFrame no mesmo arquivo com ';' como separador
    df_sem_duplicatas.to_csv(nome_arquivo, sep=';', index=False)

if __name__ == "__main__":
    # Substitua 'seu_arquivo.csv' pelo nome do seu arquivo CSV
    arquivo = 'exames.csv'

    remove_linhas_duplicadas(arquivo)

    print(f"Linhas duplicadas removidas. Resultado salvo em '{arquivo}'.")