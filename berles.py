from datetime import date
from autokolcsonzo import Auto


class Berles
    def __init__(self, auto: Auto, datum: date) -> None:
        self.__auto: Auto = auto
        self.__datum: date = datum


    @property
    def auto(self) -> Auto:
        return self.__auto

    @property
    def datum(self) -> date:
        return self.__datum

    def __str__(self) -> str:
        return f"{self.__datum} - {self.__auto.rendszam} ({self.__auto.tipus})"