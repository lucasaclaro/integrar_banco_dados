import sqlite3
from sqlite3 import Error

def conexao_banco():
    caminho = 'C:\\Users\\Investigação DISE\\Documents\\Lucas\\Python\\integrar_banco_dados\\controlecelulares.db'
    conexao = None
    conexao = sqlite3.connect(caminho)


    return conexao


conectar = conexao_banco()

codigo_sql = """INSERT INTO controlecelulares
        (NOMECONTATO, TELEFONECONTATO, EMAILCONTATO)
        VALUES ('teste_nome', 'teste_contato', 'teste_contato')"""

def inserir(conexao, sql):

    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as er:
        print(er)

inserir(conectar, codigo_sql)





conectar.close()
