"""
Ćwiczenie 1 — Definiowanie funkcji i wartości zwracane
Czas: ~15 minut
"""

# =============================================================
# ZADANIE 1a: Przelicznik temperatur
# =============================================================
# Napisz trzy funkcje:
# - celsius_na_fahrenheit(c) → zwraca temperaturę w °F
#   Wzór: F = C * 9/5 + 32
# - fahrenheit_na_celsius(f) → zwraca temperaturę w °C
#   Wzór: C = (F - 32) * 5/9
# - przelicz_temperature(wartosc, z_jednostki) → zwraca krotkę (wynik, jednostka_docelowa)
#   z_jednostki = "C" → przelicz na F, z_jednostki = "F" → przelicz na C
#   Dla nieznanej jednostki zwróć (None, "Nieznana jednostka")


def celsius_na_fahrenheit(c):
    # TODO: Uzupełnij
    pass


def fahrenheit_na_celsius(f):
    # TODO: Uzupełnij
    pass


def przelicz_temperature(wartosc, z_jednostki):
    # TODO: Uzupełnij (użyj dwóch powyższych funkcji)
    pass


# Testy:
print("=== Zadanie 1a: Przelicznik temperatur ===")
przypadki = [
    (0, "C"),  # oczekiwane: (32.0, "F")
    (100, "C"),  # oczekiwane: (212.0, "F")
    (32, "F"),  # oczekiwane: (0.0, "C")
    (98.6, "F"),  # oczekiwane: (37.0, "C")
    (20, "K"),  # oczekiwane: (None, "Nieznana jednostka")
]
for wartosc, jedn in przypadki:
    wynik, docelowa = przelicz_temperature(wartosc, jedn)
    if wynik is not None:
        print(f"  {wartosc}°{jedn} → {wynik:.1f}°{docelowa}")
    else:
        print(f"  {wartosc}°{jedn} → {docelowa}")

print()

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
    # TODO: Uzupełnij (bez użycia min(), max(), sum())
    pass


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

# =============================================================
# ZADANIE 1c: Funkcja zwracająca funkcję
# =============================================================
# Napisz funkcję potega_n(n) która:
# - Zwraca NOWĄ FUNKCJĘ podnoszącą argument do potęgi n
# Przykład użycia:
#   kwadrat = potega_n(2)
#   szescian = potega_n(3)
#   kwadrat(5) → 25
#   szescian(3) → 27


def potega_n(n):
    # TODO: Uzupełnij — zwróć wewnętrzną funkcję
    pass


print("=== Zadanie 1c: Funkcja zwracająca funkcję ===")
if potega_n(2) is not None:
    kwadrat = potega_n(2)
    szescian = potega_n(3)
    czwarta = potega_n(4)
    print(f"  kwadrat(5)  = {kwadrat(5)}")  # 25
    print(f"  szescian(3) = {szescian(3)}")  # 27
    print(f"  czwarta(2)  = {czwarta(2)}")  # 16
else:
    print("  TODO: Zaimplementuj potega_n()")
