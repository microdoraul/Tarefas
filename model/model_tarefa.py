from database import conectar_bd
def inserir_tarefa(texto_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute(""" 
                   INSERT INTO (tarefa, status)
                   VALUE (?, ?)
                   """,
                   [texto_tarefa, "PENDENTE"])
    conexao.commit()
    conexao.close()

    def recuperar_terefas():
            conexao, cursor = conectar_bd()
            cursor.execute("""
                        seclet * from tarefas
                        """)