from database import conectar



class DashboardService:


    @staticmethod
    def total_treinos():


        conn = conectar()

        cursor = conn.cursor()


        cursor.execute(

            "SELECT COUNT(*) FROM treinos"

        )


        resultado = cursor.fetchone()[0]


        conn.close()


        return resultado





    @staticmethod
    def total_exercicios():


        conn = conectar()

        cursor = conn.cursor()


        cursor.execute(

            "SELECT COUNT(*) FROM exercicios"

        )


        resultado = cursor.fetchone()[0]


        conn.close()


        return resultado





    @staticmethod
    def maior_carga():


        conn = conectar()

        cursor = conn.cursor()


        cursor.execute(

            "SELECT MAX(peso) FROM exercicios"

        )


        resultado = cursor.fetchone()[0]


        conn.close()



        if resultado:

            return resultado


        return 0