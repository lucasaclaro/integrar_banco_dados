import sqlite3
from sqlite3 import Error


def conexao_banco():
    caminho = 'C:\\Users\\Investigação DISE\\Documents\\Lucas\\Python\\integrar_banco_dados\\controlecelulares.db'
    conexao = None
    conexao = sqlite3.connect(caminho)

    return conexao


conectar = conexao_banco()


codigo_sql = "SELECT * FROM controlecelulares"

def consultar(conexao, sql):
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()

        return resultado

res = consultar(conectar, codigo_sql)

for registros in res:
    print(registros)



conectar.close()
