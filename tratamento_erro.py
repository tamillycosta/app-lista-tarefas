
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='tarefas'
)

cursor = conexao.cursor()

def seleciona_id():
    lista = []
    cursor.execute('SELECT id FROM tarefas')
    lista.append(cursor.fetchall())
    return lista

num = int(input('numero '))

id_disponiveis = seleciona_id()
for i in id_disponiveis:
    for j in i:
        if num in j:
            print('tem')
        else:
            print('nao tem')
