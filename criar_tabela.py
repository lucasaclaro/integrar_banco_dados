import sqlite3
from sqlite3 import Error


def conexao_banco():
    caminho = 'C:\\Users\\Investigação DISE\\Documents\\Lucas\\Python\\integrar_banco_dados\\controlecelulares.db'
    conexao = None
    conexao = sqlite3.connect(caminho)


    return conexao


conectar = conexao_banco()


codigo_sql = """CREATE TABLE controlecelulares(
            IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMECONTATO VARCHAR(30),
            TELEFONECONTATO VARCHAR(14),
            EMAILCONTATO VARCHAR(30)
        );"""

def criar_tabela(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print('Tabela criada')
    except Error as er:
        print(er)

criar_tabela(conectar, codigo_sql)



conectar.close()
