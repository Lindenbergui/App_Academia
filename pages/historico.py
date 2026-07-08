import flet as ft

from database import conectar



def historico(page, exercicio_id):


    conn = conectar()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            peso_anterior,
            peso_novo,
            data

        FROM historico_carga

        WHERE exercicio_id = ?

        ORDER BY id DESC

        """,
        (
            exercicio_id,
        )
    )


    dados = cursor.fetchall()


    conn.close()



    registros = []


    for item in dados:


        registros.append(

            ft.Card(

                content=ft.Container(

                    padding=15,

                    content=ft.Column(

                        [

                            ft.Text(
                                f"{item[0]} kg  ➜  {item[1]} kg",
                                size=18
                            ),

                            ft.Text(
                                item[2]
                            )

                        ]

                    )

                )

            )

        )



    def voltar(e):

        page.clean()

        from pages.home import home

        page.add(
            home(page)
        )



    page.clean()


    page.add(

        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=voltar

        ),


        ft.Text(

            "Histórico de carga",

            size=30,

            weight=ft.FontWeight.BOLD

        ),


        ft.Divider(),


        *registros

    )