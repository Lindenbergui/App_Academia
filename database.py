import sqlite3

from models.treino import Treino
from models.grupo import Grupo
from models.exercicio import Exercicio


DATABASE = "database/academia.db"



def conectar():

    return sqlite3.connect(DATABASE)





# =========================
# CRIAÇÃO DO BANCO
# =========================

def criar_banco():

    conn = conectar()

    cursor = conn.cursor()



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS treinos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome TEXT NOT NULL,

            descricao TEXT

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grupos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            treino_id INTEGER NOT NULL,

            nome TEXT NOT NULL,

            ordem INTEGER DEFAULT 0,

            FOREIGN KEY (treino_id)
            REFERENCES treinos(id)

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercicios (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            treino_id INTEGER,

            grupo_id INTEGER,

            nome TEXT NOT NULL,

            peso REAL DEFAULT 0,

            series INTEGER DEFAULT 4,

            repeticoes INTEGER DEFAULT 10,

            progresso INTEGER DEFAULT 0,

            FOREIGN KEY (treino_id)
            REFERENCES treinos(id),

            FOREIGN KEY (grupo_id)
            REFERENCES grupos(id)

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico_carga (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            exercicio_id INTEGER NOT NULL,

            peso_anterior REAL,

            peso_novo REAL,

            data TEXT,

            FOREIGN KEY (exercicio_id)
            REFERENCES exercicios(id)

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS configuracoes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome_usuario TEXT

        )
    """)



    conn.commit()

    conn.close()





# =========================
# DADOS INICIAIS
# =========================

def popular_banco():

    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        "SELECT COUNT(*) FROM treinos"
    )


    quantidade = cursor.fetchone()[0]



    if quantidade == 0:


        cursor.execute("""
            INSERT INTO treinos
            (
                nome,
                descricao
            )

            VALUES

            (
                'Treino A',
                'Costas • Bíceps • Trapézio'
            ),

            (
                'Treino B',
                'Peito • Tríceps • Ombro'
            ),

            (
                'Treino C',
                'Pernas'
            )

        """)



    conn.commit()

    conn.close()





# =========================
# TREINOS
# =========================

def listar_treinos():

    conn = conectar()

    cursor = conn.cursor()



    cursor.execute("""
        SELECT

            id,

            nome,

            descricao


        FROM treinos
    """)



    dados = cursor.fetchall()



    conn.close()



    treinos = []



    for linha in dados:


        treinos.append(

            Treino(

                id=linha[0],

                nome=linha[1],

                descricao=linha[2]

            )

        )



    return treinos





def adicionar_treino(nome, descricao):

    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO treinos

        (

            nome,

            descricao

        )

        VALUES (?, ?)

        """,

        (

            nome,

            descricao

        )

    )



    conn.commit()

    conn.close()





def editar_treino(

    treino_id,

    nome,

    descricao

):


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        UPDATE treinos

        SET

            nome = ?,

            descricao = ?


        WHERE id = ?

        """,

        (

            nome,

            descricao,

            treino_id

        )

    )



    conn.commit()

    conn.close()





def excluir_treino(treino_id):

    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        DELETE FROM exercicios

        WHERE treino_id = ?

        """,

        (

            treino_id,

        )

    )



    cursor.execute(
        """
        DELETE FROM grupos

        WHERE treino_id = ?

        """,

        (

            treino_id,

        )

    )



    cursor.execute(
        """
        DELETE FROM treinos

        WHERE id = ?

        """,

        (

            treino_id,

        )

    )



    conn.commit()

    conn.close()





# =========================
# GRUPOS
# =========================

def listar_grupos(treino_id):

    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT

            id,

            treino_id,

            nome,

            ordem


        FROM grupos


        WHERE treino_id = ?


        ORDER BY ordem, id

        """,

        (

            treino_id,

        )

    )



    dados = cursor.fetchall()



    conn.close()



    grupos = []



    for linha in dados:


        grupos.append(

            Grupo(

                id=linha[0],

                treino_id=linha[1],

                nome=linha[2],

                ordem=linha[3]

            )

        )



    return grupos


def contar_exercicios_grupo(grupo_id):

    conn = conectar()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT COUNT(*)

        FROM exercicios

        WHERE grupo_id = ?

        """,

        (
            grupo_id,

        )

    )


    quantidade = cursor.fetchone()[0]


    conn.close()


    return quantidade


def adicionar_grupo(

    treino_id,

    nome

):


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO grupos

        (

            treino_id,

            nome

        )


        VALUES (?, ?)

        """,

        (

            treino_id,

            nome

        )

    )



    conn.commit()

    conn.close()

# =========================
# EDITAR / EXCLUIR GRUPOS
# =========================


def editar_grupo(

    grupo_id,

    nome

):

    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        UPDATE grupos

        SET

            nome = ?


        WHERE id = ?

        """,

        (

            nome,

            grupo_id

        )

    )



    conn.commit()

    conn.close()





def excluir_grupo(grupo_id):

    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        DELETE FROM exercicios

        WHERE grupo_id = ?

        """,

        (

            grupo_id,

        )

    )



    cursor.execute(
        """
        DELETE FROM grupos

        WHERE id = ?

        """,

        (

            grupo_id,

        )

    )



    conn.commit()

    conn.close()





# =========================
# EXERCÍCIOS
# =========================


def adicionar_exercicio(

    treino_id,

    nome,

    peso,

    series,

    repeticoes,

    grupo_id=None

):


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO exercicios

        (

            treino_id,

            grupo_id,

            nome,

            peso,

            series,

            repeticoes

        )


        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (

            treino_id,

            grupo_id,

            nome,

            peso,

            series,

            repeticoes

        )

    )



    conn.commit()

    conn.close()





def listar_exercicios(treino_id):


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT

            id,

            treino_id,

            grupo_id,

            nome,

            peso,

            series,

            repeticoes,

            progresso


        FROM exercicios


        WHERE treino_id = ?

        """,

        (

            treino_id,

        )

    )



    dados = cursor.fetchall()



    conn.close()



    exercicios = []



    for linha in dados:


        exercicios.append(

            Exercicio(

                id=linha[0],

                treino_id=linha[1],

                grupo_id=linha[2],

                nome=linha[3],

                peso=linha[4],

                series=linha[5],

                repeticoes=linha[6],

                progresso=linha[7]

            )

        )



    return exercicios





def editar_exercicio(

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





def excluir_exercicio(exercicio_id):


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





def atualizar_progresso_exercicio(exercicio_id):


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        UPDATE exercicios


        SET progresso =


            CASE


                WHEN progresso < 4

                THEN progresso + 1


                ELSE progresso


            END



        WHERE id = ?

        """,

        (

            exercicio_id,

        )

    )



    conn.commit()

    conn.close()

# =========================
# HISTÓRICO
# =========================


def salvar_historico(

    exercicio_id,

    peso_anterior,

    peso_novo,

    data

):


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO historico_carga

        (

            exercicio_id,

            peso_anterior,

            peso_novo,

            data

        )


        VALUES (?, ?, ?, ?)

        """,

        (

            exercicio_id,

            peso_anterior,

            peso_novo,

            data

        )

    )



    conn.commit()

    conn.close()





def listar_historico(exercicio_id):


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT

            peso_novo


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



    valores = []



    for item in dados:


        valores.append(

            item[0]

        )



    return valores





# =========================
# USUÁRIO
# =========================


def salvar_usuario(nome):


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(

        "DELETE FROM configuracoes"

    )



    cursor.execute(
        """
        INSERT INTO configuracoes

        (

            nome_usuario

        )


        VALUES (?)

        """,

        (

            nome,

        )

    )



    conn.commit()

    conn.close()





def buscar_usuario():


    conn = conectar()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT

            nome_usuario


        FROM configuracoes


        LIMIT 1

        """
    )



    resultado = cursor.fetchone()



    conn.close()



    if resultado:


        return resultado[0]



    return "Usuário"