from .base import Classe


class Clerigo(Classe):
    """Representa a classe Clérigo no RPG."""

    def __init__(self):
        super().__init__(
            nome="Clérigo",
            dado_vida="1d8",
            armaduras="Todas exceto armaduras pesadas",
            armas="Armas simples (sem corte)"
        )

    def habilidades(self) -> str:
        return (
            "Conjura magias divinas (Sabedoria).\n"
            "Pode expulsar mortos-vivos.\n"
            "Restrição: não usa armas cortantes."
        )
