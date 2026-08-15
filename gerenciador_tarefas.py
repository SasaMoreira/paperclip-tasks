# Importando funcionalidades do arquivo de conexão (conexaoDataBase)
from conexaoDataBase import (
    inserir_tarefa,
    buscar_tarefas,
    marcar_como_concluida,
    deletar_tarefa,
)

# Função de adicinar tarefas
def adicionar_tarefa(): 
    
    tarefa = input("Digite aqui sua tarefa:")
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
        print("Você precisa digitar o valor de uma tarefa existente:")
        return

 
    
    marcar_como_concluida(id_tarefa)
    print(f"Tarefa concluída!\n")


def excluir_tarefa():
    listar_tarefas()

    try:
        id_tarefa = int(input("digite o ID da tarefa que deseja deletar:"))
    except ValueError:
        print("Digite um número válido.")
        return

    deletar_tarefa(id_tarefa)
    print(f"A tarefa {id_tarefa} foi excluida.")
    


# Iniciando a rotina principal
print("Bem vindo ao gerenciador de tarefas")
while True: 

    print("---------- 📎 Gerenciador de Tarefas 📎 ----------\n")

    print("1 - Adicionar Tarefa")
    print("2 - Listar tarefas existentes")
    print("3 - Finalize uma tarefa (Marcar como concluída)")
    print("4 - Exclua uma tarefa (apagar)")
    print("5 - Fechar o programa\n")
 
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
        print("Opção Inválida. Por favor, digite um número!")

    