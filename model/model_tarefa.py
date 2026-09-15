from database.conexao import conectar_bd

def inserir_tarefa(texto_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute(""" 
                   INSERT INTO tarefas (tarefa, status)
                   VALUES (?, ?);
                   """,
                   [texto_tarefa, "PENDENTE"])
    conexao.commit()
    cod_tarefa = cursor.lastrowid
    conexao.close()
    return cod_tarefa

def recuperar_terefas():
    conexao, cursor = conectar_bd()
    cursor.execute("""
                        select * from tarefas;
                        """)
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

def deletar_tarefa(codigo_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute("""
    delete from tarefa where cod_tarefa = ?;
    """, [codigo_tarefa])
    conexao.commit()
    conexao.close()

