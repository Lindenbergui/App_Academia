import flet as ft



class TreinoCard(ft.Container):


    def __init__(
        self,
        nome,
        descricao,
        abrir,
        editar,
        excluir
    ):


        super().__init__()



        self.padding = 20

        self.margin = 10

        self.border_radius = 20

        self.bgcolor = ft.Colors.BLUE_GREY_50



        self.content = ft.Column(

            [

                ft.Row(

                    [

                        ft.Icon(

                            ft.Icons.FITNESS_CENTER,

                            size=32

                        ),



                        ft.Text(

                            nome,

                            size=24,

                            weight=ft.FontWeight.BOLD,

                            color=ft.Colors.BLACK

                        )

                    ]

                ),



                ft.Text(

                    descricao,

                    size=16,

                    color=ft.Colors.GREY_700

                ),




                ft.Container(

                    height=10

                ),




                ft.Row(

                    [

                        ft.FilledButton(

                            content=ft.Text(

                                "▶ Iniciar"

                            ),

                            on_click=abrir

                        ),



                        ft.OutlinedButton(

                            content=ft.Text(

                                "✏ Editar"

                            ),

                            on_click=editar

                        ),



                        ft.OutlinedButton(

                            content=ft.Text(

                                "🗑 Excluir"

                            ),

                            on_click=excluir

                        )

                    ],


                    wrap=True,

                    spacing=8

                )

            ],

            spacing=8

        )