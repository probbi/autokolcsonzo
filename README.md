[![Elevator Pitch](https://pub-91da716c25164a4a9bb1755980b809e1.r2.dev/K%C3%A9perny%C5%91k%C3%A9p_20260415_145814.png)](https://pub-735e280475974f1e814498324f63acd9.r2.dev/HH303S.mp4)
Kérlek kattints a képre ha szeretnéd megtekinteni az Elevator Pitch videót!
# Autókölcsönző Rendszer

Ez a projekt egy egyszerű, konzolos autókölcsönző alkalmazás Python nyelven. A célja egy valósághű példa bemutatása objektumorientált programozási alapokkal.

A rendszer lehetővé teszi az autók kölcsönzését, a bérlések lemondását és az aktuális bérlések listázását. Kétféle járműtípus szerepel benne: személyautó és teherautó. A projekt induláskor már tartalmaz 3 autót és 4 kezdeti bérlést, így rögtön használatra kész. A rendszer azt is kezeli, ha egy autó már foglalt az adott napra, illetve hibát jelez nem létező bérlés lemondásakor.

## Funkciók

- autó hozzáadása a kölcsönzőhöz
- autó bérlése adott dátumra
- bérlés lemondása
- aktuális bérlések listázása
- személyautók és teherautók kezelése
- hibakezelés foglalt autókra és nem létező bérlésekre

## Osztályok

- `Auto` – absztrakt alap osztály
- `SzemelyAuto` – személyautó típus
- `TeherAuto` – teherautó típus
- `AutoKolcsonzo` – a kölcsönző működését kezeli
- `Berles` – egy konkrét bérlést tárol

## Használat

A program egy egyszerű menüs felületen keresztül használható:

1. Autó bérlése  
2. Bérlés lemondása  
3. Bérlések listázása  
4. Kilépés  

## Futtatás

A projekt a `main.py` fájlból indítható a következő paranccsal: `python main.py`

## Követelmények

- Python 3.14 vagy kompatibilis verzió
- külső csomagokra nincs szükség

## Megjegyzés

A projekt az objektumorientált programozás gyakorlására készült, és tartalmaz absztrakt osztályt, öröklődést, property-ket, non-public attribútumokat és kivételkezelést.