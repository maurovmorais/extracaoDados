from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyodbc import Error
import sql
import time
from datetime import date, datetime
import conecta

# Inicio Execução
started = datetime.now()
print("Inicio Execução: ",started)

# Data Sistema
data = str(date.today())

# Criar objeto Navegador
navegador = webdriver.Chrome()

# Abrir site google Pesqusiar Dolar
def CotacaoDolar(navegador_dolar):
    navegador.get(navegador_dolar)

    # Fazer a Pesquisa Cotação do Dolar
    navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys("cotação dólar")

    # Clicar enter
    navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.ENTER)

    # Pegar o valor da cotação do dolar
    cotacao_dolar=navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    return cotacao_dolar

# Abrir site google Pesquisar Euro
def CotacaoEuro(navegador_euro):
    navegador.get(navegador_euro)

    # Fazer a Pesquisa Cotação do Euro
    navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys("cotação euro")

    # Clicar enter
    navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.ENTER)

    # Pegar o valor da cotação do Euro
    cotacao_euro=navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    return cotacao_euro

# Abrir site google Pesquisar Ouro
def CotacaoOuro(navegador_ouro):
    navegador.get(navegador_ouro)

    # Pegar o valor da cotação do ouro
    cotacao_ouro=navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
    cotacao_ouro=cotacao_ouro.replace(",",".")

    return cotacao_ouro


# Chama as funções
cotacao_dolar = CotacaoDolar('https://www.google.com.br/')
cotacao_euro = CotacaoEuro('https://www.google.com.br/')
cotacao_ouro = CotacaoOuro('https://www.melhorcambio.com/ouro-hoje')

# Inserir dados na Tabela do Banco de Dados
vcon=conecta.ConexaoBanco()

# Query
vsql  = f"""insert into cotacaoMoedas(data,cotacao_dolar,cotacao_euro,cotacao_ouro) 
	values('{data}','{cotacao_dolar}','{cotacao_euro}','{cotacao_ouro}')"""

def inserte(conexao,sql):  
    try: 
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Dado inserido !!!")
    except Error as ex:
        print(f"Erro encontrado !!!!",ex)
 
inserte(vcon,vsql)

# Fechar Conexão
if True:
    vcon.close()
    print("Conexão fechada")

# Fechar o Browser
navegador.quit()

# Fim Execução
finished = datetime.now()
print("Fim Execução: ",finished)