from database import (
    listar_treinos,
    adicionar_treino,
    excluir_treino,
    editar_treino
)



class TreinoService:



    @staticmethod
    def listar():

        return listar_treinos()



    @staticmethod
    def adicionar(nome, descricao):

        adicionar_treino(

            nome,

            descricao

        )



    @staticmethod
    def editar(

        treino_id,

        nome,

        descricao

    ):

        editar_treino(

            treino_id,

            nome,

            descricao

        )



    @staticmethod
    def excluir(treino_id):

        excluir_treino(

            treino_id

        )
