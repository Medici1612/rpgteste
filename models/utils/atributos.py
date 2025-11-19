import random
from typing import Dict, List


class Status:
    """Representa os atributos principais de um personagem."""

    def __init__(self, forca: int, destreza: int, constituicao: int, inteligencia: int, sabedoria: int, carisma: int):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    @classmethod
    def from_dict(cls, valores: Dict[str, int]) -> "Status":
        return cls(
            forca=valores.get("Força", 0),
            destreza=valores.get("Destreza", 0),
            constituicao=valores.get("Constituição", 0),
            inteligencia=valores.get("Inteligência", 0),
            sabedoria=valores.get("Sabedoria", 0),
            carisma=valores.get("Carisma", 0),
        )

    def to_dict(self) -> Dict[str, int]:
        return {
            "Força": self.forca,
            "Destreza": self.destreza,
            "Constituição": self.constituicao,
            "Inteligência": self.inteligencia,
            "Sabedoria": self.sabedoria,
            "Carisma": self.carisma,
        }


# ================== MÉTODOS WEB ================== #

class MetodoGeracao:
    """Interface para métodos de geração de atributos para Flask (sem prints/input)."""

    def gerar(self) -> Status:
        raise NotImplementedError


class MetodoClassico(MetodoGeracao):
    """Método Clássico: 3d6 em ordem."""

    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def gerar(self) -> Status:
        valores = {
            "Força": self._rolar_3d6(),
            "Destreza": self._rolar_3d6(),
            "Constituição": self._rolar_3d6(),
            "Inteligência": self._rolar_3d6(),
            "Sabedoria": self._rolar_3d6(),
            "Carisma": self._rolar_3d6(),
        }
        return Status.from_dict(valores)


class MetodoLivre(MetodoGeracao):
    """Método Aventureiro: 3d6 seis vezes, distribuição automática (melhores valores nos atributos mais impactantes)."""

    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def gerar(self) -> Status:
        rolagens = sorted([self._rolar_3d6() for _ in range(6)], reverse=True)

        # Algoritmo simples e funcional:
        # distribui os maiores valores nos atributos mais usados
        atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

        valores = {atributos[i]: rolagens[i] for i in range(6)}

        return Status.from_dict(valores)


class MetodoHeroico(MetodoGeracao):
    """Método Heróico: 4d6 drop lowest, distribuição automática."""

    def _rolar_4d6_drop1(self) -> int:
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.remove(min(dados))
        return sum(dados)

    def gerar(self) -> Status:
        rolagens = sorted([self._rolar_4d6_drop1() for _ in range(6)], reverse=True)

        atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        valores = {atributos[i]: rolagens[i] for i in range(6)}

        return Status.from_dict(valores)
