
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='tarefas'
)

cursor = conexao.cursor()

# ADICIONA TAREFA AO BANCO DE DADOS

def adicionar_tarefas(descrição):
    sql = 'INSERT INTO tarefas (descricao,concluido) VALUES (%s,%s)'
    valores = (descrição,False)
    cursor.execute(sql,valores)
    conexao.commit()


# OBTER TODAS AS TAREFAS DO BANCO DE DADOS
def obter_tarefas():
    sql = 'SELECT * FROM tarefas'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado


# DETERMINAR AS TAREFAS COMO CONCLUIDAS
def concluida(id_tarefa):
    sql = 'UPDATE tarefas SET concluido = True WHERE id = "%s" '
    valores = (id_tarefa,)
    cursor.execute(sql,valores)
    conexao.commit()


# DELETA TAREFA DO BANCO DE DADOS
def deleta_tarefa(id_tarefa):
    sql = 'DELETE FROM tarefas WHERE id = "%s" '
    valores = (id_tarefa)
    cursor.execute(sql,valores)
    conexao.commit()



