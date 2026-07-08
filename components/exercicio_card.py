import flet as ft



class ExercicioCard(ft.Container):


    def __init__(
        self,
        exercicio,
        registrar,
        editar=None,
        excluir=None,
        grafico=None
    ):


        super().__init__()



        self.padding = 15

        self.border_radius = 15

        self.bgcolor = ft.Colors.BLUE_GREY_50



        progresso = exercicio.progresso



        if progresso >= 4:

            texto_concluir = "✅ Concluído"

        else:

            texto_concluir = "✓ Concluir"




        self.content = ft.Column(

            [


                ft.Row(

                    [

                        ft.Icon(

                            ft.Icons.FITNESS_CENTER,

                            size=28

                        ),



                        ft.Text(

                            exercicio.nome,

                            size=20,

                            weight=ft.FontWeight.BOLD

                        )

                    ]

                ),




                ft.Text(

                    f"🏋️ {exercicio.peso} kg   |   {exercicio.series} séries x {exercicio.repeticoes} repetições",

                    size=15

                ),




                ft.ProgressBar(

                    value=progresso / 4

                ),




                ft.Text(

                    f"Progresso: {progresso}/4",

                    size=14

                ),




                ft.Row(

                    [

                        ft.FilledButton(

                            content=ft.Text(

                                texto_concluir

                            ),

                            on_click=registrar,

                            disabled=progresso >= 4

                        ),




                        ft.IconButton(

                            icon=ft.Icons.EDIT,

                            tooltip="Editar",

                            on_click=editar

                        ) if editar else ft.Container(),




                        ft.IconButton(

                            icon=ft.Icons.DELETE,

                            tooltip="Excluir",

                            on_click=excluir

                        ) if excluir else ft.Container(),




                        ft.IconButton(

                            icon=ft.Icons.SHOW_CHART,

                            tooltip="Gráfico",

                            on_click=grafico

                        ) if grafico else ft.Container()

                    ],

                    wrap=True

                )

            ],

            spacing=8

        )