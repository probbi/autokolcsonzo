from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: float) -> None:
        self.__rendszam: str = rendszam
        self.__tipus: str = tipus
        self.__berleti_dij: float = berleti_dij
        self.__elerheto: bool = True

    @property
    def rendszam(self) -> str:
        return self.__rendszam

    @property
    def tipus(self) -> str:
        return self.__tipus

    @property
    def berleti_dij(self) -> float:
        return self.__berleti_dij

    @property
    def elerheto(self) -> bool:
        return self.__elerheto

    @elerheto.setter
    def elerheto(self, ertek: bool) -> None:
        self.__elerheto = ertek

    @abstractmethod
    def berleti_dij_szamitas(self) -> float:
        pass


class SzemelyAuto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: float, utasszam: int) -> None:
        super().__init__(rendszam, tipus, berleti_dij)
        self.__utasszam: int = utasszam

    def berleti_dij_szamitas(self) -> float:
        return self.berleti_dij


class TeherAuto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: float, teherbiras: int) -> None:
        super().__init__(rendszam, tipus, berleti_dij)
        self.__teherbiras: int = teherbiras

    def berleti_dij_szamitas(self) -> float:
        return self.berleti_dij * 1.1  # Példa: a teherautó bérlése drágább
