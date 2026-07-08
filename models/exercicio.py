from dataclasses import dataclass


@dataclass
class Exercicio:


    id: int

    treino_id: int

    grupo_id: int

    nome: str

    peso: float

    series: int

    repeticoes: int

    progresso: int