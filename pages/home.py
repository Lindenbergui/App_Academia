import flet as ft

from components.treino_card import TreinoCard
from services.treino_service import TreinoService
from pages.treino import tela_treino
from database import buscar_usuario



def home(page: ft.Page):


    usuario = buscar_usuario()

    cards = []



    def atualizar():

        page.clean()

        page.add(

            home(page)

        )

        page.update()




    def abrir_treino(treino):

        tela_treino(

            page,

            treino.nome,

            treino.descricao,

            treino.id

        )




    def excluir(treino):


        def confirmar(e):


            TreinoService.excluir(

                treino.id

            )


            page.overlay.remove(dialog)


            page.update()


            atualizar()




        def cancelar(e):


            page.overlay.remove(dialog)

            page.update()





        dialog = ft.Container(


            width=350,

            padding=20,

            border_radius=15,

            bgcolor=ft.Colors.BLUE_GREY_50,


            content=ft.Column(

                [

                    ft.Text(

                        "Excluir treino?",

                        size=22,

                        weight=ft.FontWeight.BOLD,

                        color=ft.Colors.BLACK

                    ),



                    ft.Text(

                        f"Excluir {treino.nome}?\nTodos os exercícios serão removidos.",

                        color=ft.Colors.BLACK

                    ),



                    ft.Row(

                        [

                            ft.TextButton(

                                content=ft.Text(

                                    "Cancelar"

                                ),

                                on_click=cancelar

                            ),



                            ft.FilledButton(

                                content=ft.Text(

                                    "Excluir"

                                ),

                                on_click=confirmar

                            )

                        ],

                        alignment=ft.MainAxisAlignment.END

                    )

                ]

            )

        )



        page.overlay.append(dialog)

        page.update()





    def editar(treino):


        from pages.editar_treino import editar_treino


        editar_treino(

            page,

            treino,

            atualizar

        )






    for treino in TreinoService.listar():


        cards.append(


            TreinoCard(

                treino.nome,

                treino.descricao,


                lambda e, t=treino:

                    abrir_treino(t),



                lambda e, t=treino:

                    editar(t),



                lambda e, t=treino:

                    excluir(t)

            )

        )





    def abrir_perfil(e):

        from pages.perfil import perfil

        perfil(page)





    def abrir_dashboard(e):

        from pages.dashboard import dashboard

        dashboard(page)





    def abrir_novo_treino(e):

        from pages.novo_treino import novo_treino

        novo_treino(page)





    return ft.Column(


        controls=[


            ft.Row(

                [

                    ft.Column(

                        [

                            ft.Text(

                                "💪 Treino+",

                                size=36,

                                weight=ft.FontWeight.BOLD

                            ),



                            ft.Text(

                                f"Olá, {usuario}! Vamos treinar hoje?",

                                size=18,

                                color=ft.Colors.GREY_700

                            )

                        ]

                    ),



                    ft.IconButton(

                        icon=ft.Icons.PERSON,

                        on_click=abrir_perfil

                    )

                ],

                alignment=ft.MainAxisAlignment.SPACE_BETWEEN

            ),




            ft.Divider(),




            ft.Text(

                "Meus treinos",

                size=24,

                weight=ft.FontWeight.BOLD

            ),




            *cards,





            ft.FilledButton(

                content=ft.Text(

                    "📊 Abrir Dashboard"

                ),

                on_click=abrir_dashboard

            ),





            ft.FilledButton(

                content=ft.Text(

                    "➕ Novo Treino"

                ),

                on_click=abrir_novo_treino

            )

        ],



        spacing=15,

        scroll=ft.ScrollMode.AUTO

    )