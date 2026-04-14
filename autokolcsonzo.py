from abc import ABC, abstractmethod
class AutoKolcsonzo(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: float): -> None:
        self.__rendszam: str = rendszam
        self.__tipus: str = tipus
        self.__berleti_dij: float = berleti_dij
        self.__elerheto: bool = True
