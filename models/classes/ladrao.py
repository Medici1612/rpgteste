from .base import Classe


class Ladrao(Classe):
    """Representa a classe Ladrão no RPG."""

    def __init__(self):
        super().__init__(
            nome="Ladrão",
            dado_vida="1d6",
            armaduras="Leves",
            armas="Leves"
        )

    def habilidades(self) -> str:
        return (
            "Furtividade, abrir fechaduras, detectar armadilhas.\n"
            "Ataque furtivo com dano extra ao surpreender inimigos."
        )
