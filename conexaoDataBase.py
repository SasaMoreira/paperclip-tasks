import os
import psycopg2
from dotenv import load_dotenv

# Carregando as variáveis do arquivo .env para o programa
load_dotenv()


def conectar():
    # Estabelecendo conexão com o banco de dados; Pegando as variaveis de .env
    try:
        conexao = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            database = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"), 
            port = os.getenv("DB_PORT")
        )
        return conexao
    except psycopg2.OperationalError as erro:
        print("Não foi possível conectar ao banco de dados.")
        print(f"Detelhe do erro: {erro}")
        return None



def inserir_tarefa(conteudo_tarefa):
    # Atribuindo a função conectar a variavel
    conexao = conectar()
    # Testando se a conexão retornou nula e exibir mensagem de erro
    if conexao == None:
        print("Não foi possivel estabelecer a conexão ")
        return
    
    # Criando objeto que vai interagir com nosso banco
    interacao = conexao.cursor()

    # Executando nosso comando SQL que vai inserir as tarefas do python p/ tabela postgresql
    interacao.execute(
        "INSERT INTO tarefas (conteudo_tarefa) VALUES (%s)",
        (conteudo_tarefa,)
    )
    # Salvando nosso comando
    conexao.commit()

    # Fechando o cursor e fechando a conexao
    interacao.close()
    conexao.close()

#Busca todas as tarefas cadastradas no banco de dados
def buscar_tarefas():
    conexao = conectar()

    if conexao == None:
        print("Algo deu errado na conexão.")
        return
    
    cursor = conexao.cursor()

    # Buscando os status da tarefa
    cursor.execute("SELECT id, conteudo_tarefa, esta_feita FROM tarefas ORDER BY id")
    
    # Retornando os resultados da query em formato de tuplas
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado

#Função que marcará como feita
def marcar_como_concluida(id_tarefa):
    conexao = conectar()

    if conexao == None:
            print("Algo deu errado na conexão.")
            return

    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE tarefas SET esta_feita = True WHERE id = %s",
        (id_tarefa,)
    )

    #Verificando a quantidade de linhas que foram adicionadas ou removidas no banco
    linhas_afetadas = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()

    # As linhas afetadas devem ser maiores que 0 para que se entenda que houve uma modificação com um id existente
    return linhas_afetadas > 0

# Função que vai apagar a tarefa
def deletar_tarefa(id_tarefa):
    conexao = conectar()

    if conexao == None:
            print("Algo deu errado na conexão.")
            return
    
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = %s",
        (id_tarefa,)
    )

    linhas_afetadas = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()

    return linhas_afetadas > 0
    


if __name__ == "__main__":
    # Teste rápido: insere uma tarefa e depois lista todas
    inserir_tarefa("Testar conexao com o banco")
    tarefas = buscar_tarefas()

    print("Tarefas no banco:")
    for tarefa in tarefas:
        print(tarefa)




        