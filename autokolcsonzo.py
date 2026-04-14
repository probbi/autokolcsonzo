from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: float): -> None
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

    @berleti_dij.setter
    def berleti_dij(self, berleti_dij: float) -> None:
        if ertek < 0:
            raise ValueError("A bérleti díj nem lehet negatív!")
        self.__berleti_dij = ertek


    @property
    def elerheto(self) -> bool:
        return self.__elerheto


    @elerheto.setter
    def elerheto(self, elerheto: bool) -> None:
        self.__elerheto = ertek


    @abstractmethod
    def berleti_dij_szamitas(self) -> float:
        pass

    abstractmethod
    def berleti_dij_szamitas(self) -> float:
        pass

