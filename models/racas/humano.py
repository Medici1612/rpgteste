from .base import Raca


class Humano(Raca):
    """Representa a raça Humano no RPG."""

    def __init__(self):
        super().__init__(
            nome="Humano",
            movimento=9,
            infravisao=False,
            alinhamento="Qualquer"
        )

    def habilidades(self) -> str:
        return (
            "Aprendizado: +10% em toda XP recebida.\n"
            "Adaptabilidade: +1 em uma Jogada de Proteção à escolha."
        )
