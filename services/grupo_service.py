from database import (
    listar_grupos,
    adicionar_grupo,
    editar_grupo,
    excluir_grupo,
    contar_exercicios_grupo
)



class GrupoService:



    @staticmethod
    def listar(treino_id):

        return listar_grupos(

            treino_id

        )




    @staticmethod
    def adicionar(

        treino_id,

        nome

    ):

        adicionar_grupo(

            treino_id,

            nome

        )




    @staticmethod
    def editar(

        grupo_id,

        nome

    ):

        editar_grupo(

            grupo_id,

            nome

        )




    @staticmethod
    def excluir(

        grupo_id

    ):

        excluir_grupo(

            grupo_id

        )




    @staticmethod
    def contar_exercicios(

        grupo_id

    ):

        return contar_exercicios_grupo(

            grupo_id

        )