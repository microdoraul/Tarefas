import flet as ft
import sqlite3 
from classe_campo_incluir import Campo_incluir
from database.conexao import criar_banco_dados
from model import model_tarefa

def main(page:ft.Page):
    page.title = "Armazenamendo de Tarefas"
    page.bgcolor = "#44ff00"
    page.horizontal_alignment = "center"
    page.window.width = 800
    page.window.height = 800

    #criando a tabela de tarefas no banco de dados SQLITE3
    conexao, cursor = conectar_bd()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tarefas( 
                   cod_tarefas INTEGER PRIMARY KEY AUTOINCREMENT,
                   tarefa TEXT,
                   status TEXT);
                   """)
    conexao.commit() 
    conexao.close()

    title = ft.Text(value="Analisardor De Tarefas ✔",size=30,font_family="Arial",)
    lista_incluir = []
    def excluir_campo (campo_tarefa):
        lista_incluir.remove(campo_tarefa)

    def adicionar_campo():
        model_tarefa.inserir_tarefa(campo_tarefas.value)
        novo_campo = Campo_incluir(texto_tarefa=campo_tarefas.value,
                                   funcao_excluir=excluir_campo)
        lista_incluir.append(novo_campo)
        

        #criando a tabela de tarefas no banco de dados SQLITE3
        conexao.cursor = conectar_bd()
        cursor.execute("""
                    INSERT INTO tarefas (tarefa, status)
                       VALUES (?, ?);
                   """,
                   [campo_tarefas.value, "PENDENTE"])
        conexao.commit() 
        conexao.close()
        campo_tarefas.value = ""




    button_excluir = ft.FloatingActionButton(icon=ft.Icon(ft.Icons.DELETE_FOREVER,
                                                          color="#000"),
                                                          bgcolor="#fff",
                                                          hover_color="#0000ff")

    button_incluir = ft.Button(content="Incluir",
                               on_click=adicionar_campo,)
    

    campo_tarefas = ft.TextField(value="",
                                 label="Tarefas",
                                 text_align="center",
                                 on_submit=adicionar_campo)

    

    linha_começo = ft.Row(controls=[campo_tarefas, button_incluir],
                          alignment="center",
                          spacing=50)
    
    container = ft.Container(content=linha_começo,
                             bgcolor="#1adba4",
                             padding=30,
                             border_radius=20,
                             width=550,
                             height=100)

    coluna_tarefas = ft.Column(controls=lista_incluir,
                               horizontal_alignment="center")





    page.controls = [title,container, coluna_tarefas]
    page.spacing = 45
    page.update()

ft.run(main)