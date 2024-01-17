import time
import pyautogui
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Abrir o navegador e acessar o site do SISREG.
driver = webdriver.Chrome()
driver.get("https://sisregiii.saude.gov.br/")

# Adicionando informações de login e senha.
pyautogui.alert(text='Responda o catpcha e aperte OK para continuar', title='Confirmações', button='OK')
driver.find_element(By.NAME, "entrar").click()

# Entrar na página de confirmação.
driver.get("https://sisregiii.saude.gov.br/cgi-bin/cons_agendas")

#Selecionar as opções corretas no menu.
pyautogui.alert(text='Preencha o formulário corretamente e aperte ok.', title='Confirmações', button='OK')
driver.find_element(By.NAME, "btnOK").click()
time.sleep(10)

# Descobrindo e buscando chaves:
def buscandochaves(cod_chave, cod_xpath):
    elementos_chave = driver.find_elements(By.NAME, cod_chave)
    if elementos_chave:
        buscarchave = str(driver.find_element(By.XPATH, cod_xpath).text)
        with open('chaves.csv', mode='r') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                solicitacao = str(linha[0])
                chave = str(linha[1])
                if solicitacao == buscarchave and chave:
                    driver.find_element(By.NAME, cod_chave).clear()
                    driver.find_element(By.NAME, cod_chave).send_keys(chave)
                    chaves_adicionadas = chaves_adicionadas + 1
                    return chaves_adicionadas
    else:
        print('Elemento não encontrando, buscando outras chaves para pesquisar') 

# Pergunta o número total de páginas para buscar.
total_paginas = 1
        
while True:
    chaves_adicionadas = 0
    buscandochaves('Chave0', '//*[@id="tblConfirmacao0"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave1', '//*[@id="tblConfirmacao1"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave2', '//*[@id="tblConfirmacao2"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave3', '//*[@id="tblConfirmacao3"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave4', '//*[@id="tblConfirmacao4"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave5', '//*[@id="tblConfirmacao5"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave6', '//*[@id="tblConfirmacao6"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave7', '//*[@id="tblConfirmacao7"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave8', '//*[@id="tblConfirmacao8"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave9', '//*[@id="tblConfirmacao9"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave10', '//*[@id="tblConfirmacao10"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave11', '//*[@id="tblConfirmacao11"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave12', '//*[@id="tblConfirmacao12"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave13', '//*[@id="tblConfirmacao13"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave14', '//*[@id="tblConfirmacao14"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave15', '//*[@id="tblConfirmacao15"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave16', '//*[@id="tblConfirmacao16"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave17', '//*[@id="tblConfirmacao17"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave18', '//*[@id="tblConfirmacao18"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave19', '//*[@id="tblConfirmacao19"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave20', '//*[@id="tblConfirmacao20"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave21', '//*[@id="tblConfirmacao21"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave22', '//*[@id="tblConfirmacao22"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave23', '//*[@id="tblConfirmacao23"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave24', '//*[@id="tblConfirmacao24"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave25', '//*[@id="tblConfirmacao25"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave26', '//*[@id="tblConfirmacao26"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave27', '//*[@id="tblConfirmacao27"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave28', '//*[@id="tblConfirmacao28"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave29', '//*[@id="tblConfirmacao29"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave30', '//*[@id="tblConfirmacao30"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave31', '//*[@id="tblConfirmacao31"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave32', '//*[@id="tblConfirmacao32"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave33', '//*[@id="tblConfirmacao33"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave34', '//*[@id="tblConfirmacao34"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave35', '//*[@id="tblConfirmacao35"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave36', '//*[@id="tblConfirmacao36"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave37', '//*[@id="tblConfirmacao37"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave38', '//*[@id="tblConfirmacao38"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave39', '//*[@id="tblConfirmacao39"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave40', '//*[@id="tblConfirmacao40"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave41', '//*[@id="tblConfirmacao41"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave42', '//*[@id="tblConfirmacao42"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave43', '//*[@id="tblConfirmacao43"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave44', '//*[@id="tblConfirmacao44"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave45', '//*[@id="tblConfirmacao45"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave46', '//*[@id="tblConfirmacao46"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave47', '//*[@id="tblConfirmacao47"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave48', '//*[@id="tblConfirmacao48"]/tbody/tr[1]/td[1]/center/b')
    buscandochaves('Chave49', '//*[@id="tblConfirmacao49"]/tbody/tr[1]/td[1]/center/b') 
    if chaves_adicionadas == 0:
        total_paginas = total_paginas + 1
        driver.find_element(By.XPATH, '//*[@id="main_page"]/form/center[3]/table/tbody/tr/td/input').clear()
        driver.find_element(By.XPATH, '//*[@id="main_page"]/form/center[3]/table/tbody/tr/td/input').send_keys(str(total_paginas))
        pyautogui.press('enter')
        time.sleep(10)
    else: 
        pyautogui.alert(text='Responda o catpcha e aperte OK para finalizar', title='Confirmações', button='OK')
        driver.find_element(By.NAME, "btnConfirmar").click()
        total_paginas = total_paginas + 1
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="main_page"]/form/center[3]/table/tbody/tr/td/input').clear()
        driver.find_element(By.XPATH, '//*[@id="main_page"]/form/center[3]/table/tbody/tr/td/input').send_keys(str(total_paginas))
        pyautogui.press('enter')
        time.sleep(10)
