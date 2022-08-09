import sqlite3
from sqlite3 import Error


def conexao_banco():
    caminho = 'C:\\Users\\Investigação DISE\\Documents\\Lucas\\Python\\integrar_banco_dados\\controlecelulares.db'
    conexao = None
    conexao = sqlite3.connect(caminho)

    return conexao


conectar = conexao_banco()


codigo_sql = "UPDATE controlecelulares SET NOMECONTATO = 'bruno' WHERE IDCONTATO=1"

def atualizar(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print('Dados atualizados')
    except Error as er:
        print(er)

atualizar(conectar, codigo_sql)



conectar.close()
