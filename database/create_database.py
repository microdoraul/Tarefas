from database.conexao import conetar_bd

def criar_banco_dedos()
    conexao, cursor = conectar_bd()
    cursor.execute(""" 
                    create table if not exists tarefas(
                   cod_tarefas integer primary key autoincrement
                   tarefa text
                   status text )
                   """,
                   [texto_tarefa, "PENDENTE"])
    conexao.commit()
    conexao.close()