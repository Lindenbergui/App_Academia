from database import conectar



class GraficoService:


    @staticmethod
    def carregar(exercicio_id):

        conn = conectar()

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT
                peso_novo,
                data

            FROM historico_carga

            WHERE exercicio_id = ?

            ORDER BY id

            """,
            (
                exercicio_id,
            )
        )


        dados = cursor.fetchall()


        conn.close()


        return dados