# Importando funcionalidades do arquivo de conexão (conexaoDataBase)
from conexaoDataBase import (
    inserir_tarefa,
    buscar_tarefas,
    marcar_como_concluida,
    deletar_tarefa,
)

# Função de adicinar tarefas
def adicionar_tarefa(): 
    # Input de tarefa sem espaços 
    tarefa = input("Digite aqui sua tarefa:")
    # Barrando tarefas vazias
    if not tarefa:
        print('Você inseriu um valor vazio. Digite a tarefa que você deseja!')
        return
    else:
        inserir_tarefa(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso! ✅")
    

# Definindo a função LISTAR_TAREFAS 
def listar_tarefas():
    # Buscando as tarefas no banco, nos dando o ID do banco, não o índice do python
    tarefas = buscar_tarefas()

    if not tarefas:
        print("Não há nenhuma tarefa cadastrada ainda.")
        return
    
    print("\n 📎 Lista de Tarefas: ")

    # Verificando o status e exibindo
    for i in tarefas:
        id_tarefa, conteudo_tarefa, esta_feita = i
        if esta_feita:
            status = "Feita ✔️"  
        else: status = "Pendente ⏳"
        print(f"{id_tarefa} - {conteudo_tarefa} ({status})")

def concluir_tarefa():
    listar_tarefas()

    # Solicita ao usuário o ID da tarefa a ser finalizada
    try:
        id_tarefa = int(input("Digite o número da tarefa que deseja finalizar: "))
    except ValueError:
        print("Ops! Parece que você digitou algo além de apenas o número de id.📎\nPara que possamos prosseguir, digite apenas o numero da tarefa que vai concluir.")
        return

    #Verificando se de fato houve pelo menos uma alteração no database
    # para que o usuario nao consiga terminar uma tarefa inexistente.
    alteracao = marcar_como_concluida(id_tarefa)
    if alteracao == True:
        print(f"Tarefa {id_tarefa} foi marcada como concluida! ♡♡♡\n")
    else:
        print(f"A tarefa {id_tarefa} não existe ainda.📎\nPor favor, verifique o id da tarefa e tente novamente.")
    

def excluir_tarefa():
    listar_tarefas()

    try:
        id_tarefa = int(input("digite o ID da tarefa que deseja deletar:"))
    except ValueError:
        print("Ops! Parece que você digitou algo além de apenas o número de id.📎\nPara que possamos prosseguir, digite apenas o numero da tarefa que vai excluir.")
        return
    

    alteracao = deletar_tarefa(id_tarefa)

    if alteracao == True:
        print(f"A tarefa {id_tarefa} foi excluida.")
    else: 
        print(f"A tarefa {id_tarefa} não foi concluida porque ela não existe ainda.📎\nPor favor verifique o id e tente novamente! 📎")
       


# Iniciando a rotina principal
print("♡ Bem vindo ao gerenciador de tarefas PaperClip ♡\n")

while True: 
    print(" Gerenciador de tarefas 📎 \n")
    print("1 - Adicionar Tarefa")
    print("2 - Listar tarefas existentes")
    print("3 - Finalize uma tarefa (Marcar como concluída)")
    print("4 - Exclua uma tarefa (apagar)")
    print("5 - Fechar o programa\n")
    try:
        opcao = int(input("---------- Digite a opção desejada: ---------- "))
    
        if opcao == 1:
            adicionar_tarefa()

        elif opcao == 2:
            listar_tarefas()

        elif opcao == 3:
            concluir_tarefa()

        elif opcao == 4:
            excluir_tarefa()

        elif opcao == 5:
            print("Saindo do programa")
            break
        else:
            print("Opção Inválida. Por favor, digite um número! 📎")
    except ValueError:
        print("Ops! Parece que você digitou algo além de um número.\nPara prosseguir, por favor, digite o número de uma das opções do menu.")