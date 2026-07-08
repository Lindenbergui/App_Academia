import flet as ft

from services.dashboard_service import DashboardService



def dashboard(page: ft.Page):


    total_treinos = DashboardService.total_treinos()

    total_exercicios = DashboardService.total_exercicios()

    maior_carga = DashboardService.maior_carga()



    def voltar(e):

        from pages.home import home


        page.clean()


        page.add(

            home(page)

        )





    def card(titulo, valor, icone):


        return ft.Container(


            padding=20,

            border_radius=20,

            bgcolor=ft.Colors.BLUE_GREY_50,


            content=ft.Column(

                [

                    ft.Text(

                        icone,

                        size=32

                    ),



                    ft.Text(

                        titulo,

                        size=16,

                        color=ft.Colors.GREY_700

                    ),



                    ft.Text(

                        str(valor),

                        size=30,

                        weight=ft.FontWeight.BOLD,

                        color=ft.Colors.BLACK

                    )

                ]

            )

        )





    page.clean()



    page.add(



        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=voltar

        ),




        ft.Text(

            "📊 Dashboard",

            size=32,

            weight=ft.FontWeight.BOLD

        ),




        ft.Text(

            "Resumo dos seus treinos",

            size=18,

            color=ft.Colors.GREY_700

        ),




        ft.Divider(),




        ft.Row(

            [

                card(

                    "Treinos",

                    total_treinos,

                    "💪"

                ),



                card(

                    "Exercícios",

                    total_exercicios,

                    "🏋️"

                )

            ],

            wrap=True

        ),




        ft.Row(

            [

                card(

                    "Maior carga",

                    f"{maior_carga} kg",

                    "📈"

                )

            ],

            wrap=True

        )

    )