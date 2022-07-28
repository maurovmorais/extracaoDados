from pickle import TRUE
from re import T
from sql import connect

vcon=connect.ConexaoBanco()

#Query
vsql = """Select * from Vendas"""

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



