from functions_banco_dados import  *
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='tarefas'
)

cursor = conexao.cursor()


def erro_input(mensagem=""):
    while True:
        try:
            opcao = int(input(mensagem))
            if 1 <= opcao <= 5:
                return opcao
        except (NameError,ValueError):
            print('Sinto muito, mas seu codigo esta invalido')


# EXCESSÃO PERSONALIZADA
class IDInvalidoException(Exception):
    def __init__(self, message="ID inválido. \nDigite um ID válido."):
        self.message = message
        super().__init__(self.message)


 # SELECIONAR  UM ID DO BANCO DE DADOS
def seleciona_id():
    lista = []
    cursor.execute('SELECT id FROM tarefas')
    lista.append(cursor.fetchall())
    return lista


# TRATAR INPUT DA OPCAO 4
def tratamento_opcao_4():
    id_disponiveis = seleciona_id()
    while True:
        try:
            tarefa_id = int(input('informe com o id '))

            for i in id_disponiveis:
                for j in i:
                    if tarefa_id in j:
                        print('tarefa excluida com sucesso')
                        return deleta_tarefa(tarefa_id)
            raise IDInvalidoException()
        except IDInvalidoException as e:
            print(e)
            print('')
        except ValueError:
            print('Digite um ID válido!')

def tratamento_opcao_3():
    id_disponivel = seleciona_id()
    while True:
        try:
            tarefa_id = int(input('selecione a tarefa que deseja pelo ID '))

            for i in id_disponivel:
                for j in i:
                    if tarefa_id in j:
                        print(' tarefa concluida co sucesso!')
                        return concluida(tarefa_id)
                    if len(id_disponivel) == 0:
                        print(' nenhuma tarefa no sistema')

            raise IDInvalidoException()
        except IDInvalidoException as e:
            print(e)
            print('')
        except ValueError:
            print('Digite um ID válido!')
