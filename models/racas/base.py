from abc import ABC, abstractmethod


class Raca(ABC):
    """
    Classe base para todas as raças do RPG.
    Define atributos comuns e exige implementação do método habilidades().
    """

    def __init__(self, nome: str, movimento: int, infravisao: bool, alinhamento: str):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento

    @abstractmethod
    def habilidades(self) -> str:
        """Retorna as habilidades especiais da raça."""
        pass

    def resumo(self) -> str:
        """Retorna um resumo formatado da raça."""
        infravisao_txt = "Sim" if self.infravisao else "Não"
        return (
            f"Raça: {self.nome}\n"
            f"Movimento: {self.movimento}m\n"
            f"Infravisão: {infravisao_txt}\n"
            f"Alinhamento: {self.alinhamento}\n"
        )
