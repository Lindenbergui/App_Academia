from dataclasses import dataclass


@dataclass
class Historico:

    id: int

    exercicio_id: int

    peso_anterior: float

    peso_novo: float

    data: str