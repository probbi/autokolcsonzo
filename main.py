from datetime import date
from autokolcsonzo import SzemelyAuto, TeherAuto
from auto_kolcsonzo import AutoKolcsonzo


def main() -> None:
    kolcsonzo = AutoKolcsonzo("FullCar Autókölcsönző")

    # 3 autó hozzáadása
    kolcsonzo.auto_hozzaadasa(SzemelyAuto("JPN-123", "Suzuki Swift", 10000, 5))
    kolcsonzo.auto_hozzaadasa(TeherAuto("GRM-456", "Fiat Ducato", 15000, 5))
    kolcsonzo.auto_hozzaadasa(SzemelyAuto("ITA-747", "Alfa Romeo Stelvio", 35000, 5))

    # 4 kezdeti bérlés (különböző dátumokkal)
    kezdeti_berlesek = [
        ("ITA-747", date(2026, 4, 20)),
        ("ITA-747", date(2026, 4, 22)),
        ("JPN-123", date(2026, 5, 21)),
        ("GRM-456", date(2026, 6, 22)),
    ]

    for rsz, datum in kezdeti_berlesek:
        try:
            kolcsonzo.auto_berlese(rsz, datum)
        except ValueError as e:
            print(f"Kezdeti hiba: {e}")

    while True:
        print("\n--- MENÜ ---")
        print("1. Autó bérlése\n2. Bérlés lemondása\n3. Listázás\n4. Kilépés")
        v = input("Válasszon: ")

        if v == "1":
            rsz = input("Rendszám: ")
            d_str = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                ev, ho, nap = map(int, d_str.split("-"))
                dij = kolcsonzo.auto_berlese(rsz, date(ev, ho, nap))
                print(f"Sikeres! Díj: {dij} Ft")
            except Exception as e:
                print(f"Hiba: {e}")

        elif v == "2":
            rsz = input("Rendszám: ")
            d_str = input("Dátum: ")
            try:
                ev, ho, nap = map(int, d_str.split("-"))
                kolcsonzo.berles_lemondasa(rsz, date(ev, ho, nap))
                print("Lemondva.")
            except Exception as e:
                print(f"Hiba: {e}")

        elif v == "3":
            kolcsonzo.berlesek_listazasa()
        elif v == "4":
            break


if __name__ == "__main__":
    main()
