oceny_studentow = {
    "Anna": 5, "Bartek": 4, "Celina": 5, "Damian": 3,
    "Ewa": 4, "Filip": 2, "Grażyna": 5, "Hanna": 3
}

def odwroc_slownik(slownik):
    odwrocony = {}

    for imie, ocena in slownik.items():
        odwrocony.setdefault(ocena, []).append(imie)
        
    # odwrocony = {value : key for key, value in slownik.items()}
    return odwrocony

print("Inwersja słownika ocen:")
wynik2 = odwroc_slownik(oceny_studentow)
if wynik2:
    for ocena in sorted(wynik2, reverse=True):
        print(f"  Ocena {ocena}: {sorted(wynik2[ocena])}")