from database import salvar_historico, listar_historico

from datetime import datetime



class HistoricoService:



    @staticmethod
    def salvar(

        exercicio_id,

        peso_anterior,

        peso_novo

    ):


        salvar_historico(

            exercicio_id,

            peso_anterior,

            peso_novo,

            datetime.now().strftime(
                "%d/%m/%Y"
            )

        )




    @staticmethod
    def listar(exercicio_id):

        return listar_historico(

            exercicio_id

        )