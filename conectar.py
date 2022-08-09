import sqlite3
from sqlite3 import Error



#criar conexão com o banco de dados

def conexao_banco():
    caminho = 'C:\\Users\\Investigação DISE\\Documents\\Lucas\\Python\\integrar_banco_dados\\controlecelulares.db'
    conexao = None
    conexao = sqlite3.connect(caminho)

    return conexao

conectar = conexao_banco()

conectar.close()






