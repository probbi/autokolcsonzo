from datetime import date
from autokolcsonzo import Auto, SzemelyAuto, TeherAuto # Minden innen jön!
from berles import Berles


class AutoKolcsonzo:
    def __init__(self, nev: str) -> None:
        self.__nev: str = nev
        self.__autok: list[SzemelyAuto | TeherAuto] = []
        self.__berlesek: list[Berles] = []

    @property
    def nev(self) -> str:
        return self.__nev

    def auto_hozzaadasa(self, auto: SzemelyAuto | TeherAuto) -> None:
        self.__autok.append(auto)

    def auto_berlese(self, rendszam: str, datum: date) -> float:
        for auto in self.__autok:
            if auto.rendszam == rendszam:
                if not auto.elerheto:
                    raise ValueError("Ez az autó már foglalt!")
                auto.elerheto = False
                berles = Berles(auto, datum)
                self.__berlesek.append(berles)
                return auto.berleti_dij_szamitas()

        raise ValueError("Nem található ilyen rendszámú autó")

    def berles_lemondasa(self, rendszam: str, datum: date | None = None) -> None:
        for berles in self.__berlesek:
            if berles.auto.rendszam == rendszam and (datum is None or berles.datum == datum):
                berles.auto.elerheto = True
                self.__berlesek.remove(berles)
                return

        raise ValueError("Nem található ilyen rendszámú bérlés!")

    def berlesek_listazasa(self) -> None:
        if not self.__berlesek:
            print("Nincs aktív bérlés")
            return

        for berles in self.__berlesek:
            print(berles)
