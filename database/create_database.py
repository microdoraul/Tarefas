from database.conexao import conectar_bd

def criar_banco_dados():
    conexao, cursor = conectar_bd()
    cursor.execute(""" 
                create table if not exists tarefas(
                   cod_tarefas integer primary key autoincrement,
                   tarefa text,
                   status text)""")
    conexao.commit()
    conexao.close()