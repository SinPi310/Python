# =============================================================
# ZADANIE 1b: Statystyki listy
# =============================================================
# Napisz funkcję statystyki(liczby) która:
# - Przyjmuje listę liczb
# - Zwraca SŁOWNIK z kluczami:
#   "min", "max", "suma", "srednia", "zakres" (max - min), "ilosc"
# - Dla pustej listy zwraca None
# UWAGA: NIE używaj wbudowanych min/max/sum — zaimplementuj ręcznie!


def statystyki(liczby):
    if len(liczby) > 0:

        obecne_min = liczby[0]
        obecne_max = liczby[0]
        suma = 0
        ilosc = 0

        def min(liczby):
            return liczby[1]
    
        def max(liczby):
            return liczby[len(liczby) - 1]
    
        def srednia(liczby):

            def suma():
                for liczba in liczby:
                    wynik += liczba
                return wynik
    
            srednia = wynik / len(liczby)
            return srednia
    else:
        return None

    return {
        "min": obecne_min,
        "max": obecne_max,
        "suma": suma,
        "srednia": srednia,
        "zakres": zakres,
        "ilosc": ilosc
    }


print("=== Zadanie 1b: Statystyki listy ===")
dane_testowe = [
    [4, 8, 15, 16, 23, 42],
    [100],
    [-5, 0, 5],
    [],
]
for dane in dane_testowe:
    wynik = statystyki(dane)
    if wynik:
        print(f"  {dane}")
        for klucz, wartosc in wynik.items():
            print(f"    {klucz}: {wartosc}")
    else:
        print(f"  {dane} → None")

print()