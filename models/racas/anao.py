from .base import Raca


class Anao(Raca):
    """Representa a raça Anão no RPG."""

    def __init__(self):
        super().__init__(
            nome="Anão",
            movimento=6,
            infravisao=True,
            alinhamento="Tendem à Ordem"
        )

    def habilidades(self) -> str:
        return (
            "Mineradores: detectam anomalias em pedra (1 em 1d6, ou 1-2 se procurando).\n"
            "Vigoroso: +1 em testes de Constituição.\n"
            "Restrição: não usam armas grandes (exceto raciais).\n"
            "Inimigos: ataques contra orcs, ogros e hobgoblins são fáceis."
        )
