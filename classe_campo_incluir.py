import flet as ft

class Campo_incluir(ft.Row):
    def __int__(self, texto_tarefa):
        super().__init__()
        self.caixa_texto = ft.TextField(
            value=texto_tarefa,
            label="insira o texto",
            filled=True,
        )
        self.caixa_selecao= ft.Checkbox(on_change=self.alterar_cor)
        self.amarzem = ft.Container(content=ft.Row(controls=[self.caixa_selecao,
                                                            self.caixa_texto]),
                                                             height=75,
                                                             border_radius=10,
                                                             padding=6,
                                                             bgcolor="#123456",
                                                             animate=ft.Animation(duration=500))
        self.button_delete=ft.Button(
            content="Delete",
            width=100,
            on_click=lambda:self.funcao_excluir(self))
        
        self.nutton_edit=ft.Button(content="Edit",
                                   width=100)
        self.linhas_buttons = ft.Column(controls=[self.button_delete, self.nutton_edit])

        self.controls = [self.amarzem, self.linhas_buttons]

    def alterar_cor(self):
        if self.caixa_selecao.value == True:
            self.amarzem.bgcolor = "#654321"

        else:
            self.amarzem.bgcolor = "#123456"

    @property
    def value(self):
        return self.caixa_texto.value    
