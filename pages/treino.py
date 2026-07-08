import flet as ft

from services.grupo_service import GrupoService
from components.grupo_card import GrupoCard



def tela_treino(page, treino_nome, descricao, treino_id):


    def abrir_grupo(grupo):

        from pages.grupo import tela_grupo


        tela_grupo(

            page,

            grupo,

            treino_nome,

            descricao,

            treino_id

        )





    def recarregar():

        tela_treino(

            page,

            treino_nome,

            descricao,

            treino_id

        )





    def editar_grupo(grupo):


        campo = ft.TextField(

            label="Nome do grupo",

            value=grupo.nome

        )



        def salvar(e):


            if campo.value:


                GrupoService.editar(

                    grupo.id,

                    campo.value

                )


                dialog.open = False

                page.update()


                recarregar()



        dialog = ft.AlertDialog(


            title=ft.Text(

                "Editar grupo muscular"

            ),


            content=campo,


            actions=[


                ft.TextButton(

                    "Salvar",

                    on_click=salvar

                )

            ]

        )



        page.overlay.append(dialog)

        dialog.open = True

        page.update()





    def excluir_grupo(grupo):


        def confirmar(e):


            GrupoService.excluir(

                grupo.id

            )


            dialog.open = False

            page.update()


            recarregar()



        def fechar(e):

            dialog.open = False

            page.update()



        dialog = ft.AlertDialog(


            title=ft.Text(

                "Excluir grupo?"

            ),



            content=ft.Text(

                f"Excluir {grupo.nome} e todos os exercícios?"

            ),



            actions=[


                ft.TextButton(

                    "Cancelar",

                    on_click=fechar

                ),



                ft.TextButton(

                    "Excluir",

                    on_click=confirmar

                )

            ]

        )



        page.overlay.append(dialog)

        dialog.open = True

        page.update()





    def carregar_grupos():


        cards = []


        grupos = GrupoService.listar(

            treino_id

        )



        for grupo in grupos:


            quantidade = GrupoService.contar_exercicios(

                grupo.id

            )



            cards.append(


                GrupoCard(

                    grupo,


                    quantidade,



                    lambda e, g=grupo:

                        abrir_grupo(g),



                    lambda e, g=grupo:

                        editar_grupo(g),



                    lambda e, g=grupo:

                        excluir_grupo(g)

                )

            )


        return cards





    def adicionar_grupo(e):


        campo = ft.TextField(

            label="Nome do grupo muscular"

        )





        def salvar(ev):


            if campo.value:


                GrupoService.adicionar(

                    treino_id,

                    campo.value

                )


                dialog.open = False

                page.update()


                recarregar()



        dialog = ft.AlertDialog(


            title=ft.Text(

                "Novo grupo muscular"

            ),


            content=campo,


            actions=[


                ft.TextButton(

                    "Salvar",

                    on_click=salvar

                )

            ]

        )



        page.overlay.append(dialog)

        dialog.open = True

        page.update()





    def voltar(e):


        from pages.home import home


        page.clean()


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

            treino_nome,

            size=32,

            weight=ft.FontWeight.BOLD

        ),



        ft.Text(

            descricao,

            size=16

        ),



        ft.Divider(),



        ft.Text(

            "💪 Grupos musculares",

            size=22,

            weight=ft.FontWeight.BOLD

        ),



        *carregar_grupos(),



        ft.FilledButton(

            content=ft.Text(

                "➕ Novo Grupo"

            ),

            on_click=adicionar_grupo

        )

    )