from abc import ABC, abstractmethod


class Classe(ABC):
    """
    Classe base para todas as classes do RPG.
    Define atributos comuns e exige implementação do método habilidades().
    """

    def __init__(self, nome: str, dado_vida: str, armaduras: str, armas: str):
        self.nome = nome
        self.dado_vida = dado_vida
        self.armaduras = armaduras
        self.armas = armas

    @abstractmethod
    def habilidades(self) -> str:
        """Retorna as habilidades especiais da classe."""
        pass

    def resumo(self) -> str:
        """Retorna um resumo formatado da classe."""
        return (
            f"Classe: {self.nome}\n"
            f"Dado de Vida: {self.dado_vida}\n"
            f"Armaduras: {self.armaduras}\n"
            f"Armas: {self.armas}\n"
        )
