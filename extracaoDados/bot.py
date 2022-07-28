from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import date

# Criar objeto Navegador
navegador = webdriver.Chrome()

# Abrir site google
navegador.get('https://www.google.com.br/')

#Fazer a Pesquisa Cotação do Dolar
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

# Clicar enter
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# Pegar o valor da cotação do dolar
cotacao_dolar=navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

# Abrir site google
navegador.get('https://www.google.com.br/')

#Fazer a Pesquisa Cotação do Euro
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

# Clicar enter
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# Pegar o valor da cotação do Euro
cotacao_euro=navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)

# Abrir site google
navegador.get('https://www.melhorcambio.com/ouro-hoje')

# Pegar o valor da cotação do ouro
cotacao_ouro=navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro=cotacao_ouro.replace(",",".")
print(cotacao_ouro)

# Fechar o Browser
navegador.quit()

# Salvar pesquisa no Excel

tabela =  pd.read_excel(r"C:\Projetos\extracaoDados\extracaoDados\cotacaoMoedas_Outro.xlsx")

tabela.loc[1,"data"] = date.today()
tabela.loc[1,"dolar"] = float(cotacao_dolar)
tabela.loc[1,"euro"] = float(cotacao_euro)
tabela.loc[1,"ouro"] = float(cotacao_ouro)


tabela.to_excel("C:\Projetos\extracaoDados\extracaoDados\cotacaoMoedas_Outro.xlsx",index=False)

