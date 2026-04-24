"""
Ćwiczenie 2 — Parametry zaawansowane
Czas: ~15 minut
"""

# =============================================================
# ZADANIE 2a: Funkcja z wartościami domyślnymi
# =============================================================
# Napisz funkcję formatuj_adres() z parametrami:
#   ulica, numer, miasto, kod_pocztowy, kraj="Polska"
# Zwraca sformatowany adres jako string:
#   "ul. Kwiatowa 15\n00-001 Warszawa\nPolska"
#
# Dodaj walidację: jeśli ulica, numer lub miasto jest puste/None
# → zwróć "Błąd: niekompletny adres"


def formatuj_adres(ulica, numer, miasto, kod_pocztowy, kraj="Polska"):
    if not ulica or not numer or not miasto :
        return "Błąd: niekompletny adres"
    return f"ul. {ulica} {numer}\n{kod_pocztowy} {miasto}\n{kraj}"


print("=== Zadanie 2a: Formatowanie adresu ===")
print(formatuj_adres("Kwiatowa", "15", "Warszawa", "00-001"))
print()
print(formatuj_adres("Main Street", "42", "Berlin", "10115", kraj="Niemcy"))
print()
print(formatuj_adres(None, "5", "Kraków", "30-001"))  # Błąd

print()

# =============================================================
# ZADANIE 2b: Funkcja z *args
# =============================================================
# Napisz funkcję srednia_wazona(*oceny_wagi) która:
# - Przyjmuje pary (ocena, waga) jako argumenty pozycyjne
#   np. srednia_wazona((5, 3), (4, 2), (3, 1))
# - Oblicza średnią ważoną: Σ(ocena*waga) / Σ(waga)
# - Zwraca wynik zaokrąglony do 2 miejsc po przecinku
# - Dla pustych argumentów zwraca 0.0


def srednia_wazona(*oceny_wagi):
    # TODO: Uzupełnij
    pass


print("=== Zadanie 2b: Średnia ważona ===")
print(f"  {srednia_wazona((5, 3), (4, 2), (3, 1))}")  # 4.33
print(f"  {srednia_wazona((2, 1), (5, 1))}")  # 3.5
print(f"  {srednia_wazona()}")  # 0.0

print()

# =============================================================
# ZADANIE 2c: Funkcja z **kwargs — budowanie zapytania SQL
# =============================================================
# Napisz funkcję buduj_zapytanie(tabela, **warunki) która:
# - Buduje prosty string zapytania SELECT
# - tabela — nazwa tabeli
# - **warunki — pary kolumna=wartość dla klauzuli WHERE
# - Jeśli brak warunków → "SELECT * FROM tabela;"
# - Jeśli są warunki → "SELECT * FROM tabela WHERE k1='v1' AND k2='v2';"
#   (wartości string w apostrofach, liczby bez)


def buduj_zapytanie(tabela, **warunki):
    # TODO: Uzupełnij
    pass


print("=== Zadanie 2c: Budowanie zapytań ===")
print(f"  {buduj_zapytanie('uzytkownicy')}")
# SELECT * FROM uzytkownicy;
print(f"  {buduj_zapytanie('produkty', kategoria='elektronika', cena=100)}")
# SELECT * FROM produkty WHERE kategoria='elektronika' AND cena=100;
print(f"  {buduj_zapytanie('zamowienia', status='aktywne', klient_id=42)}")
# SELECT * FROM zamowienia WHERE status='aktywne' AND klient_id=42;

print()

# =============================================================
# ZADANIE 2d: Rozpakowywanie argumentów
# =============================================================
# Dana jest lista słowników z konfiguracją serwerów.
# Napisz funkcję polacz_z_serwerem(host, port, protokol, timeout=30)
# która zwraca string: "Łączę: {protokol}://{host}:{port} (timeout={timeout}s)"
#
# Następnie użyj rozpakowywania (**), aby wywołać tę funkcję
# dla KAŻDEGO elementu z listy serwery.


def polacz_z_serwerem(host, port, protokol, timeout=30):
    # TODO: Uzupełnij
    pass


serwery = [
    {"host": "192.168.1.1", "port": 443, "protokol": "https"},
    {"host": "10.0.0.5", "port": 22, "protokol": "ssh", "timeout": 10},
    {"host": "db.local", "port": 5432, "protokol": "postgres", "timeout": 60},
]

print("=== Zadanie 2d: Rozpakowywanie argumentów ===")
for serwer in serwery:
    # TODO: Wywołaj polacz_z_serwerem z rozpakowaniem słownika
    pass  # Zamień na: print(f"  {polacz_z_serwerem(**serwer)}")
