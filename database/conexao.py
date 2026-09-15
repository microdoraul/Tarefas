def conetar_bd():
    conexao = sqlite3.connect("bd_tarefas.sqlite")
    cursor = conexao.cursor() #criando cursor 
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tarefas( 
                   cod_tarefas INTEGER PRIMARY KEY AUTOINCREMENT,
                   tarefa TEXT,
                   status TEXT);
                   """)
    conexao.commit() 
    conexao.close()