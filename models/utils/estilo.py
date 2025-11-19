import time
from .cores import Cores


def linha(tam: int = 50, char: str = "=") -> str:
    """Retorna uma linha decorativa com o tamanho e caractere especificados."""
    return f"{Cores.AMARELO}{char * tam}{Cores.RESET}"


def titulo(texto: str) -> str:
    """Retorna um título formatado com bordas."""
    borda = linha(len(texto) + 6, "=")
    return f"\n{borda}\n{Cores.NEGRITO}{Cores.VERDE}|| {texto.upper()} ||{Cores.RESET}\n{borda}"


def bloco(texto: str) -> str:
    """Formata um bloco de texto com prefixo estilizado."""
    linhas = texto.split("\n")
    return "\n".join([f"{Cores.CYAN}   > {l}{Cores.RESET}" for l in linhas])


def pausa(seg: float = 1.0) -> None:
    """Pausa a execução por um número de segundos (default: 1.0)."""
    time.sleep(seg)
