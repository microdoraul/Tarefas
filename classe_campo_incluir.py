import flet as ft
from model import model_tarefa

class Campo_incluir(ft.Row):
    def __init__(self, texto_tarefa, funcao_excluir, cod_tarefa):
        super().__init__()

        self.cod_tarefa = cod_tarefa

        self.funcao_excluir = funcao_excluir

        self.caixa_texto = ft.TextField(value=texto_tarefa,
                                        label="insira o texto",
                                        filled=True)
        self.caixa_selecao = ft.Checkbox(on_change=self.alterar_cor)
        self.armazem = ft.Container(content=ft.Row(controls=[self.caixa_selecao,
                                                             self.caixa_texto]),
                                                             height=75,
                                                             border_radius=10,
                                                             padding=6,
                                                             bgcolor="#123456",
                                                             animate=ft.Animation(duration=500))

        self.button_delete=ft.Button(content="Delete",
                                     width=100,
                                     on_click=lambda: self.funcao_excluir(self) )
        
        self.nutton_edit=ft.Button(content="Edit",
                                   width=100,
                                   on_click=self.alterar_tarefa)
        
        self.linha_buttons = ft.Column(controls=[self.button_delete, self.nutton_edit])

        self.controls = [self.armazem,self.linha_buttons]

    def alterar_cor(self):
        if self.caixa_selecao.value == True:
            self.armazem.bgcolor = "#654321"
            model_tarefa.atualizar_status(self.cod_tarefa, "CONCLUÍDO")
        else:
            self.armazem.bgcolor = "#123456"
            model_tarefa.atualizar_status(self.cod_tarefa, "PENDENTE")
    def alterar_tarefa(self):
        model_tarefa.atualizar_tarefa(self.cod_tarefa, self.caixa_texto.value)

    @property
    def value(self):
        return self.caixa_texto.value