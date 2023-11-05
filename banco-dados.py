
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='tarefas'
)

cursor = conexao.cursor()

# CRIA BANCO DE DADOS
# cursor.execute('CREATE DATABASE tarefas')

# CRIA TABELA
cursor.execute('CREATE TABLE IF NOT EXISTS tarefas(id INT AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR(255), concluido BOOLEAN)')


