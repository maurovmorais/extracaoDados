##### Faz a conexao no Banco de Dados
import sql
import pyodbc
from pyodbc import Error

##### Criar conexão
def ConexaoBanco():
    dados_conexao = (
    "Driver={SQL Server};"
    "Server=DELLT2CN081\SQLEXPRESS;"
    "Database=PythonSQL;"
    ) 
    conn = None
    try:
        conn = pyodbc.connect(dados_conexao)
        print("Conexão Sucesso !!!")
    except Error as ex:
        print(f"Erro encontrado !!!!",ex)
    return conn
