import flet as ft

from database import listar_historico



def grafico(page, exercicio):


    valores = listar_historico(

        exercicio.id

    )


    if not valores:

        valores = [

            exercicio.peso

        ]



    pontos = []



    for valor in valores:


        pontos.append(

            {

                "valor": valor

            }

        )





    def voltar(e):


        from pages.treino import tela_treino


        page.clean()


        tela_treino(

            page,

            "Treino",

            "",

            exercicio.treino_id

        )





    linhas = []



    for i, item in enumerate(pontos):


        linhas.append(

            ft.Container(

                content=ft.Column(

                    [

                        ft.Text(

                            f"{item['valor']} kg",

                            size=12

                        ),

                        ft.Container(

                            width=35,

                            height=max(

                                20,

                                item["valor"] * 2

                            ),

                            bgcolor=ft.Colors.BLUE_400

                        ),

                        ft.Text(

                            str(i + 1)

                        )

                    ],

                    horizontal_alignment=

                    ft.CrossAxisAlignment.CENTER

                )

            )

        )





    page.clean()



    page.add(



        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=voltar

        ),




        ft.Text(

            f"Evolução - {exercicio.nome}",

            size=28,

            weight=ft.FontWeight.BOLD

        ),




        ft.Text(

            "Histórico de carga",

            size=18

        ),




        ft.Container(

            height=350,

            content=ft.Row(

                linhas,

                alignment=ft.MainAxisAlignment.CENTER,

                vertical_alignment=

                ft.CrossAxisAlignment.END,

                scroll=ft.ScrollMode.AUTO

            )

        )

    )