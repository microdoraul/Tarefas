import sqlite3
def conetar_bd():
    conexao = sqlite3.connect("bd_tarefas.sqlite")
    cursor = conexao.cursor() #criando cursor 
    return conexao, cursor