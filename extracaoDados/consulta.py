import conecta
import sql
import time
from datetime import date, datetime

# Inicio Execução
started = datetime.now()
print("Inicio Execução: ",started)

vcon=conecta.ConexaoBanco()

#Query
vsql = f"""Select * from cotacaoMoedas"""

##### Consulta Banco
def Consultar(conexao,sql): 
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()   
    return resultado

res = Consultar(vcon,vsql)
for r in res:
   print(r)

##### Fechar Conexão
if True:
    vcon.close()
    print("Conexão fechada")

# Fim Execução
finished = datetime.now()
print("Fim Execução: ",finished)
