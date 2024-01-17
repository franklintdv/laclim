import pandas as pd
import pyautogui
import cpf
import csv
import time
import sys

def obter_codigo_easylab(descricao_procedimento, correspondencias_conhecidas):
    if descricao_procedimento in correspondencias_conhecidas:
        return correspondencias_conhecidas[descricao_procedimento]
    else:
        codigo_easylab = input(f"Insira o código Easylab para '{descricao_procedimento}': ")
        correspondencias_conhecidas[descricao_procedimento] = codigo_easylab
        return codigo_easylab

# Definir o tempo para o programa aguardar para evitar erros.
pyautogui.PAUSE = 0.5

# Lista de exames que pode marcar direto.
marcar_direto = ['LEU', 'ACIF', 'ACU', 'HIV', 'HDL', 'LDL', 'COL', 'VLD', 'GLI', 'TGG', 'TGM', 'HEM', 'CBD', 'TSH', 'GSRH', 'GLI', 'FRAT', 'A1C', 'HEM', 'FER',
                 'POT', 'T3', 'T4', 'T4L', 'SOD', 'FAL', 'FOS', 'VD25', 'B12', 'TGO', 'TGP', 'SIL', 'B12', 'GGT', 'BIL', 'MAG', 'PCR', 'LDH', 'CPK', 'CAL', 'FSH', 'LH', 'EST',
                 'URE', 'RCO', 'TTPA', 'RETIC', 'LAC', 'TAP', 'TC', 'TS', 'HBA', 'HBS', 'M12', 'ALB', 'PTF', 'TES', 'PRL', 'PRG', 'PSA', 'AMI', 'PTH', 'CMM', 'CMG', 'HTLV', 'C125', 'VHS', 'INS',
                 'HBCG', 'HBCM', 'LTX', 'HBE', 'LPA', 'CEA', 'C19', 'TPO', 'EPG', 'EPM', 'CBL', 'HAV M', 'HAV G', 'RUBM', 'RUBG', 'ATG', 'CBI', 'AAE', 'CIGM', 'SHBG']

# Lista de exames para perguntar se é Futura Coleta.
perguntar_futura_coleta = ['PF', 'PF2', 'PF3', 'CUR', 'EAS', 'GPC', 'MAL', 'P24', 'M24']

# Definir a planilha que vai ser coletado os dados baixados do SIREG a serem usados.
arquivo = 'sisreg.csv'
df = pd.read_csv(arquivo, sep=';')

# Definir e carregar as planilhas com os exames.
df_exames = pd.read_csv('exames.csv', sep=';')

# Criando um dicionário para armazenar correspondências conhecidas.
correspondencias_conhecidas = dict(zip(df_exames['descricao_procedimento'], df_exames['codigo_easylab']))

# Verificando se a coluna 'codigo_easylab' existe em df.
if 'codigo_easylab' not in df.columns:
    df['codigo_easylab'] = None
    
# Substituindo os valores da coluna 'descricao_procedimento' pelo valor correspondente em 'codigo_easylab'
df['codigo_easylab'] = df.apply(
    lambda row: obter_codigo_easylab(row['descricao_procedimento'], correspondencias_conhecidas) if pd.isna(row['codigo_easylab']) else row['codigo_easylab'],
    axis=1
)

# Adicionando novas correspondências ao arquivo exames.csv
novas_correspondencias = pd.DataFrame([(descricao, codigo) for descricao, codigo in correspondencias_conhecidas.items()], columns=['descricao_procedimento', 'codigo_easylab'])
exames_atualizado = pd.concat([df_exames, novas_correspondencias], ignore_index=True)
exames_atualizado.to_csv('exames.csv', sep=';', index=False)

while True:
    # Adionar o SUS do paciente.
    CNS = pyautogui.prompt(text='Digite o número do SUS para cadastrar', title='Exames')
    # Converter a coluna CNS para string para funcionar corretamente.
    df['cns'] = df['cns'].astype(str)
    info_pessoa = df[df['cns'] == CNS]   
    if not info_pessoa.empty:
        # Pegar os códigos de e as chaves de confirmação:
        solicitacoes = info_pessoa['solicitacao'].unique()
        for solicitacao in solicitacoes:
            conferir_soliciticao = pyautogui.confirm('Pressione OK se você estiver com a solicitação: ' + str(solicitacao))
            if conferir_soliciticao == 'OK':
                chave = str(pyautogui.prompt(text='Digite o cód. de confirmação da solitação: ' + str(solicitacao), title='Exames'))
                with open('chaves.csv', 'a', newline='') as arquivo_csv:
                    escritor_csv = csv.writer(arquivo_csv)
                    escritor_csv.writerow([solicitacao, chave])
            else:
                sys.exit() 
        tem_cadastro = pyautogui.prompt(text='Tem cadastro? (s/n)', title='Exames')
        # Perguntar se tem futura coleta para agilizar o código.
        tem_futura_coleta = pyautogui.prompt(text='Tem futura coleta? (s/n)', title='Exames')
        # Perguntar se o(a) paciente é diabético(a).
        diabetico = pyautogui.prompt(text='Paciente diabético(a)? (s/n)', title='Exames', default='n')
        # Perguntar se o(a) paciente é hipertensa.
        hipertenso = pyautogui.prompt(text='Paciente hipertenso(a)? (s/n)', title='Exames', default='n')
        if tem_cadastro == 'N' or tem_cadastro == 'S':
            pyautogui.press('capslock')
        if tem_cadastro == 'n' or tem_cadastro == 'N':
            # Buscar Nome do paciente.
            nome = info_pessoa['nome'].values[0]
            print('Paciente encontrado(a): ' + nome)
            # Buscar Data de Nascimento do paciente.
            dt_nascimento = info_pessoa['dt_nascimento'].values[0]
            # Buscar sexo do paciente.
            sexo = info_pessoa['sexo'].values[0]
            # Buscar e juntas informações referentes ao Endereço do paciente.
            tipo_logradouro = str(info_pessoa['tipo_logradouro'].values[0])
            logradouro = str(info_pessoa['logradouro'].values[0])
            numero_logradouro = str(info_pessoa['numero_logradouro'].values[0])
            endereco = (tipo_logradouro or '') + " " + (logradouro or '')+ " " + ("N. " + numero_logradouro or '')
            # Buscar Bairro do(a) paciente.
            bairro = str(info_pessoa['bairro'].values[0])
            # Perguntar sobre o RG do(a) paciente.
            RG = str(pyautogui.prompt(text='Digite o número do RG para cadastrar.', title='Exames', default='0'))
            #Perguntar sobre o CPF do(a) paciente e verificar se ele é válido.
            CPF = str(pyautogui.prompt(text='Digite o número do CPF para cadastrar', title='Exames', default='0'))
            # Confirmar o endereço do(a) paciente.
            endereco = str(pyautogui.prompt(text='Digite o endereço para cadastrar.', title='Exames', default=endereco))
            # Confirmar o bairro do(a) paciente.
            bairro = str(pyautogui.prompt(text='Digite o endereço para cadastrar.', title='Exames', default=bairro))
            #Perguntar sobre o telefone do(a) paciente.
            telefone = str(info_pessoa['telefone'].values[0])
            telefone = str(pyautogui.prompt(text='Digite o número de telefone para cadastrar', title='Exames', default=telefone))
            # Apertar botão adicionar.
            pyautogui.click(x=875, y=109)
            # Preenchar a opção posto.
            pyautogui.click(x=333, y=204)
            pyautogui.write('1')
            pyautogui.press('enter')
            pyautogui.press('tab', presses=2)
            # Digitar nome.
            pyautogui.write(nome)
            pyautogui.press('tab', presses=2)
            # Digitar a data de nascimento.
            pyautogui.write(dt_nascimento)
            pyautogui.press('tab', presses=6)
            # Digitar o sexo do(a) paciente.
            pyautogui.write(sexo)
            pyautogui.press('tab', presses=2)
            # Digitar RG do(a) paciente.
            pyautogui.write(RG)
            pyautogui.press('tab')
            # Digitar CPF do(a) paciente.
            if cpf.checar(CPF) == True:
                pyautogui.write(CPF)
                pyautogui.press('tab')
            else:
                pyautogui.press('tab')
            # Digitar o CNS do(a) paciente.
            pyautogui.write(CNS)
            pyautogui.press('tab', presses=2)
            # Digitar o endereço do(a) paciente.
            pyautogui.write(endereco)
            pyautogui.press('tab', presses=2)
            # Digitar o bairro do(a) paciente.
            pyautogui.write(bairro)
            pyautogui.press('tab', presses=3)
            # Digitar o telefone do(a) paciente.
            pyautogui.write(telefone)
            # Salvar o paciente e abrir prontuario.
            pyautogui.click(x=1009, y=720)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            # Selecionar o posto e médico para continuar.
            pyautogui.alert(text='Selecione o posto e aperte Ok para continuar.', title='Exames', button='OK')
            # Confere médico.
            while True:
                try:
                    verifica_medico = pyautogui.locateOnScreen('SOLICITACAOMEDICA.PNG')
                    pyautogui.click(x=292, y=447)
                    break
                except:
                    pyautogui.doubleClick(x=891, y=447)
                    pyautogui.write('1')
                    pyautogui.press('tab')
                    pyautogui.click(x=292, y=447)
                    time.sleep(3)
                    break
            # Criar uma lista com todos os exames para serem feitos.
            exames = info_pessoa['codigo_easylab'].unique()
            print('Lista de exames do(a) paciente')
            print(exames)
            # Cadastrando o exames no sistema.
            for exame in exames:
                # 'FRH'
                if exame == 'FRH':
                    if 'GSRH' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # 'CRU'
                elif exame == 'CRU':
                    if 'MAL' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # 'CRE'
                elif exame == 'CRE':
                    if 'CLEAR' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # 'PLA'
                elif exame == 'PLA':
                    if 'HEM' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)               
                # 'TRI'
                elif exame == 'TRI':
                    if 'LDL' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write('LDL')
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # 'TS1A'
                elif exame == 'TS1A':
                    if 'CUR' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # Exames para perguntar se é futura coleta.
                elif exame in perguntar_futura_coleta:
                    if tem_futura_coleta == 's' or tem_futura_coleta == 'S':
                        futura_coleta = pyautogui.prompt(text='Exame ' + exame + ' é futura coleta? (s/n)' , title='Exames', default='n')
                    else:
                        futura_coleta = 'n'
                    if futura_coleta == 'n' or futura_coleta == 'N':
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter', presses=4)
                        pyautogui.write('F')
                        pyautogui.click(x=1265, y=461)
                # Exames para dar pause antes de continuar
                elif exame == "CLEAR" or exame == "HCV":
                    pyautogui.write(exame)
                    pyautogui.press('enter')
                    if tem_futura_coleta == 'n' or tem_futura_coleta == 'N':
                        pyautogui.click(x=1265, y=461)
                    else:
                        futura_coleta = pyautogui.prompt(text='Exame ' + exame + ' é futura coleta? (s/n)' , title='Exames', default='n')
                        if futura_coleta == 's' or futura_coleta == 'S':
                            pyautogui.press('enter', presses=3)
                            pyautogui.write('F')
                            pyautogui.click(x=1265, y=461)
                        else:
                            pyautogui.click(x=1265, y=461) 
                    time.sleep(6)
                    pyautogui.click(x=1108, y=676)
                    time.sleep(2)
                    pyautogui.click(x=768, y=496)
                # Exames para apenas adicionar.
                elif exame in marcar_direto:
                    pyautogui.write(exame)
                    pyautogui.press('enter')
                    pyautogui.click(x=1265, y=461)                   
                else:
                    exame = pyautogui.prompt(text='Código do exame para cadastrar', title='Exames', default=exame)
                    pyautogui.write(exame)
                    pyautogui.press('enter')
                    pyautogui.click(x=1265, y=461)
            # Diábetico(a), hipertens(a) e ir para informações adicionais pra adicionar.
            pyautogui.click(x=397, y=672)
            if diabetico == 'S' or diabetico == 's':
                pyautogui.write("DIAB. ")
            if hipertenso == 'S' or hipertenso == 's':
                pyautogui.write("HIPERT. ")
        else:
            # Confere médico.
            while True:
                try:
                    verifica_medico = pyautogui.locateOnScreen('SOLICITACAOMEDICA.PNG')
                    pyautogui.click(x=292, y=447)
                    break
                except:
                    pyautogui.doubleClick(x=891, y=447)
                    pyautogui.write('1')
                    pyautogui.press('tab')
                    pyautogui.click(x=292, y=447)
                    time.sleep(3)
                    break
            # Criar uma lista com todos os exames para serem feitos.
            exames = info_pessoa['codigo_easylab'].unique()
            print('Lista de exames do(a) paciente')
            print(exames)
            # Cadastrando o exames no sistema.
            for exame in exames:
                # 'FRH'
                if exame == 'FRH':
                    if 'GSRH' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # 'CRU'
                elif exame == 'CRU':
                    if 'MAL' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # 'CRE'
                elif exame == 'CRE':
                    if 'CLEAR' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # 'PLA'
                elif exame == 'PLA':
                    if 'HEM' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)                
                # 'TRI'
                elif exame == 'TRI':
                    if 'LDL' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write('LDL')
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # 'TS1A'
                elif exame == 'TS1A':
                    if 'CUR' in exames:
                        print('Cadastrado automaticamente')
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                # Exames para dar pause antes de continuar
                elif exame == "CLEAR" or exame == "HCV":
                    pyautogui.write(exame)
                    pyautogui.press('enter')
                    if tem_futura_coleta == 'n' or tem_futura_coleta == 'N':
                        pyautogui.click(x=1265, y=461)
                    else:
                        futura_coleta = pyautogui.prompt(text='Exame ' + exame + ' é futura coleta? (s/n)' , title='Exames', default='n')
                        if futura_coleta == 's' or futura_coleta == 'S':
                            pyautogui.press('enter', presses=3)
                            pyautogui.write('F')
                            pyautogui.click(x=1265, y=461)
                        else:
                            pyautogui.click(x=1265, y=461) 
                    time.sleep(6)
                    pyautogui.click(x=1108, y=676)
                    time.sleep(2)
                    pyautogui.click(x=768, y=496)
                # Exames para perguntar se é futura coleta.
                elif exame in perguntar_futura_coleta:
                    if tem_futura_coleta == 's' or tem_futura_coleta == 'S':
                        futura_coleta = pyautogui.prompt(text='Exame ' + exame + ' é futura coleta? (s/n)' , title='Exames', default='n')
                    else:
                        futura_coleta = 'n'
                    if futura_coleta == 'n' or futura_coleta == 'N':
                        pyautogui.write(exame)
                        pyautogui.press('enter')
                        pyautogui.click(x=1265, y=461)
                    else:
                        pyautogui.write(exame)
                        pyautogui.press('enter', presses=4)
                        pyautogui.write('F')
                        pyautogui.click(x=1265, y=461)
                # Exames para apenas adicionar.
                elif exame in marcar_direto:
                    pyautogui.write(exame)
                    pyautogui.press('enter')
                    pyautogui.click(x=1265, y=461)                    
                else:
                    exame = pyautogui.prompt(text='Código do exame para cadastrar', title='Exames', default=exame)
                    pyautogui.write(exame)
                    pyautogui.press('enter')
                    pyautogui.click(x=1265, y=461)
            # Diábetico(a), hipertens(a) e ir para informações adicionais pra adicionar.
            pyautogui.click(x=397, y=672)
            if diabetico == 'S' or diabetico == 's':
                pyautogui.write("DIAB. ")
            if hipertenso == 'S' or hipertenso == 's':
                pyautogui.write("HIPERT. ")
    else:
        print('Paciente não encontrado')

