import sqlite3
from sqlite3 import Error



def conexao_banco():
    caminho = 'C:\\Users\\Investigação DISE\\Documents\\Lucas\\Python\\integrar_banco_dados\\controlecelulares.db'
    conexao = None
    conexao = sqlite3.connect(caminho)


    return conexao


conectar = conexao_banco()



codigo_sql = """ DELETE FROM controlecelulares WHERE IDCONTATO=1"""

def deletar(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print('Registro deletado')
    except Error as er:
        print(er)

deletar(conectar, codigo_sql)