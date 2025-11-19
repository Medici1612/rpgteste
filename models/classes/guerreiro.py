from .base import Classe


class Guerreiro(Classe):
    """Representa a classe Guerreiro no RPG."""

    def __init__(self):
        super().__init__(
            nome="Guerreiro",
            dado_vida="1d10",
            armaduras="Todas",
            armas="Todas"
        )

    def habilidades(self) -> str:
        return (
            "BA mais rápido, pode usar todas as armas e armaduras.\n"
            "Recebe ataques extras conforme evolui."
        )
