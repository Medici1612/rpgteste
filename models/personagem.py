from models.utils.estilo import titulo, bloco, pausa, Cores
from models.racas.base import Raca
from models.classes.base import Classe
from models.utils.atributos import Status, MetodoGeracao


class Personagem:
    """
    Representa um personagem do RPG, contendo nome, raça, classe e atributos.
    """

    def __init__(self, nome: str, raca: Raca, classe: Classe, metodo: MetodoGeracao):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.atributos: Status = metodo.gerar()

    def ficha(self) -> None:
        """Exibe a ficha completa do personagem no terminal."""
        print(titulo(f"Ficha de {self.nome}"))
        print(bloco(self.atributos.resumo()))

        # Informações da Raça
        print(f"\n{Cores.AMARELO}Raça:{Cores.RESET} {self.raca.nome}")
        print(f"Alinhamento: {self.raca.alinhamento}")
        print(f"Movimento: {self.raca.movimento}m")
        print(f"Infravisão: {'Sim' if self.raca.infravisao else 'Não'}")
        print(f"Habilidades Raciais:\n{bloco(self.raca.habilidades())}\n")

        # Informações da Classe
        print(f"{Cores.AMARELO}Classe:{Cores.RESET} {self.classe.nome}")
        print(f"Dado de Vida: {self.classe.dado_vida}")
        print(f"Armaduras: {self.classe.armaduras}")
        print(f"Armas: {self.classe.armas}")
        print(f"Habilidades de Classe:\n{bloco(self.classe.habilidades())}")

        pausa(2)
