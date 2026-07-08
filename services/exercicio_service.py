from database import (
    adicionar_exercicio,
    listar_exercicios,
    atualizar_progresso_exercicio,
    conectar
)



class ExercicioService:



    @staticmethod
    def adicionar(
        treino_id,
        nome,
        peso,
        series,
        repeticoes,
        grupo_id=None
    ):


        adicionar_exercicio(

            treino_id,

            nome,

            peso,

            series,

            repeticoes,

            grupo_id

        )





    @staticmethod
    def listar(treino_id):

        return listar_exercicios(treino_id)





    @staticmethod
    def registrar_treino(exercicio_id):

        atualizar_progresso_exercicio(

            exercicio_id

        )





    @staticmethod
    def editar(
        exercicio_id,
        nome,
        peso,
        series,
        repeticoes
    ):


        conn = conectar()

        cursor = conn.cursor()



        cursor.execute(

            """
            UPDATE exercicios

            SET

                nome = ?,

                peso = ?,

                series = ?,

                repeticoes = ?,

                progresso = 0


            WHERE id = ?

            """,

            (

                nome,

                peso,

                series,

                repeticoes,

                exercicio_id

            )

        )



        conn.commit()

        conn.close()





    @staticmethod
    def excluir(exercicio_id):

        conn = conectar()

        cursor = conn.cursor()



        cursor.execute(

            """
            DELETE FROM exercicios

            WHERE id = ?

            """,

            (

                exercicio_id,

            )

        )


        conn.commit()

        conn.close()