from .base import Classe


class Mago(Classe):
    """Representa a classe Mago no RPG."""

    def __init__(self):
        super().__init__(
            nome="Mago",
            dado_vida="1d4",
            armaduras="Nenhuma",
            armas="Adagas, cajados, dardos"
        )

    def habilidades(self) -> str:
        return (
            "Conjura magias arcanas (Inteligência).\n"
            "Grande conhecimento arcano.\n"
            "Muito frágil em combate físico."
        )
