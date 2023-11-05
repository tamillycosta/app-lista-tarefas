
from functions_banco_dados import  *
from tratamento_erro import  *

def linha(mensagem=""):
    print('-'*40)
    print(mensagem.center(40))
    print('-' * 40)
    print('')


def mostrar_menu():
   linha('BEM VINDO AO MENU DE TAREFAS')
   print(' 1 - Adicionar tarefa')
   print(' 2 - Mostrar tarefas')
   print(' 3 - Marcar como concluido')
   print('4 - Excluir tarefa')
   print(' 5 - Sair')


# LOOP MENU PRINCIPAL
def menu():
   while True:
       mostrar_menu()
       print('-' * 40)
       opcao = erro_input('Oque vocẽ deseja fazer? ')

       if opcao == 1:
           linha('ADICIONAR TAREFA')

           nova_tarefa = input('informe a sua nova tarefa: ')
           adicionar_tarefas(nova_tarefa)

           print('Nova tarefa adicionada com sucesso!')
           print('')


       elif opcao == 2:
          linha('Mostrar Tarefas')

          printar_tarefas = obter_tarefas()
          if len(printar_tarefas) == 0:
              print('sem tarefas no sistema')
          else:
              for i in printar_tarefas:
                  print(f'{i[0]}. {i[1]} - {"concluida"  if i[2] else "incompleta"} ' )


       elif opcao == 3:
           linha('Marcar Como Concluido')

           printar_tarefas = obter_tarefas()
           if len(printar_tarefas) == 0:
               print(' nenhuma tarefa no sistema')
           else:
               for i in printar_tarefas:
                   print(f'{i[0]}. {i[1]} - {"concluida" if i[2] == True else "imcompleta"}')
                   tratamento_opcao_3()


       elif opcao == 4:
           linha('Excluir Tarefa')

           printar_tarefas = obter_tarefas()
           if len(printar_tarefas) == 0:
               print(' nenhuma tarefa no sistema')
           else:
               for i in printar_tarefas:
                   print(f'{i[0]}. {i[1]} - {"concluida" if i[2] == True else "imcompleta"}')
                   tratamento_opcao_4()

       elif opcao == 5:
           print('saindo 1..2..3..')
           break


