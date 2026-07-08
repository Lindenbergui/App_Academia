import flet as ft



class GrupoCard(ft.Container):


    def __init__(
        self,
        grupo,
        quantidade_exercicios,
        abrir,
        editar=None,
        excluir=None
    ):


        super().__init__()



        self.padding = 15

        self.border_radius = 15

        self.bgcolor = ft.Colors.BLUE_GREY_50



        self.content = ft.Row(

            [

                ft.Icon(

                    ft.Icons.FOLDER,

                    size=30,

                    color=ft.Colors.BLUE_GREY_700

                ),



                ft.Column(

                    [

                        ft.Text(

                            grupo.nome,

                            size=20,

                            weight=ft.FontWeight.BOLD,

                            color=ft.Colors.BLACK

                        ),



                        ft.Text(

                            f"{quantidade_exercicios} exercícios",

                            size=14,

                            color=ft.Colors.GREY_700

                        )

                    ],

                    expand=True

                ),




                ft.IconButton(

                    icon=ft.Icons.EDIT,

                    tooltip="Editar grupo",

                    on_click=editar

                ) if editar else ft.Container(),





                ft.IconButton(

                    icon=ft.Icons.DELETE,

                    tooltip="Excluir grupo",

                    on_click=excluir

                ) if excluir else ft.Container()

            ]

        )



        self.on_click = abrir