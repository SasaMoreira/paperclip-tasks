import os
import psycopg2
from dotenv import load_dotenv

# Carregando as variáveis do arquivo .env para o programa
load_dotenv()


def conectar():
    # Estabelecendo conexão com o banco de dados; Pegando as variaveis de .env
    o = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"), 
        port = os.getenv("DB_PORT")
    )
    return o


def inserir_tarefa(conteudo_tarefa):
    # Insere uma nova tarefa no banco de dados 
    conexao = conectar()
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


def buscar_tarefas():
    #Busca todas as tarefas cadastradas no banco de dados
    conexao = conectar()
    cursor = conexao.cursor()

    # Buscando os status da tarefa
    cursor.execute("SELECT id, conteudo_tarefa, esta_feita FROM tarefas ORDER BY id")
    
    # Retornando os resultados da query em formato de duplas
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado

#Função que marcará como feita
def marcar_como_concluida(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE tarefas SET esta_feita = True WHERE id = %s",
        (id_tarefa,)
    )

# Função que vai apagar a tarefa
def deletar_tarefa(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = %s",
        (id_tarefa,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()
    


if __name__ == "__main__":
    # Teste rápido: insere uma tarefa e depois lista todas
    inserir_tarefa("Testar conexao com o banco")
    tarefas = buscar_tarefas()
    marcar_como_concluida(1)

    print("Tarefas no banco:")
    for tarefa in tarefas:
        print(tarefa)




        