"""
Ćwiczenie 2 — Struktury danych
Czas: ~10 minut
"""

# =============================================================
# ZADANIE 2a: Analiza tekstu
# =============================================================
# Dana jest lista słów. Zbuduj słownik, gdzie:
# - klucze to długości słów (int)
# - wartości to listy słów o tej długości
# Wynik posortuj wg długości.

slowa = [
    "python", "java", "c", "go", "rust", "kotlin", "swift",
    "scala", "ruby", "php", "perl", "lua", "r", "julia"
]

def grupuj_po_dlugosci(slowa):
    #Torzenie słownika
    zgrupowane_slowa = {}

    #Pętla żeby dostać się do każdego słowa
    for lines in slowa:
        #Odczytujemy dłigość słowa
        dlugosc = len(lines)

        #Dodajemy słowo do słownika pod stworzunyn kluczem {dlugosc} lub tworzymy nowy klucz jeśli nie istnieje
        '''
        if dlugosc not in zgrupowane_slowa:
            zgrupowane_slowa[dlugosc] = []
        zgrupowane_slowa[dlugosc].append(slowo)
        '''
        zgrupowane_slowa[dlugosc].append(lines) if dlugosc in zgrupowane_slowa else zgrupowane_slowa.setdefault(dlugosc, []).append(lines)
    pass

    # Zwracam posortowany słownik
    return dict(sorted(zgrupowane_slowa.items()))


print("Grupowanie po długości:")
wynik = grupuj_po_dlugosci(slowa)
if wynik:
    for dl, lista in wynik.items():
        print(f"  {dl} liter: {sorted(lista)}")

print()

# =============================================================
# ZADANIE 2b: Unikalność i operacje zbiorowe
# =============================================================
# Masz dwa raporty z logami serwisów.
# Znajdź:
# a) Błędy, które wystąpiły w OBU serwisach jednocześnie
# b) Błędy TYLKO w serwisie A (nie w B)
# c) Łączna liczba UNIKALNYCH typów błędów
# d) Czy serwis B ma błędy, których BRAK w A? (True/False)

bledy_A = [404, 500, 503, 404, 401, 200, 500, 403]
bledy_B = [200, 404, 502, 503, 404, 418, 500, 502]

# TODO: Uzupełnij
bledy_A_uniq = set(bledy_A)                                     # set z unikalnych błędów A
bledy_B_uniq = set(bledy_B)                                     # set z unikalnych błędów B
wspolne = bledy_A_uniq.intersection(bledy_B_uniq)               # błędy w obu serwisach
tylko_A = bledy_A_uniq.difference(bledy_B_uniq)                 # błędy tylko w A
liczba_unikalnych = len(bledy_A_uniq | bledy_B_uniq)            # łączna liczba unikalnych typów
B_ma_unikalne = bool(bledy_B_uniq.difference(bledy_A_uniq))     # czy B ma kody nieobecne w A?

print("Analiza błędów:")
print(f"  Błędy A:                {sorted(bledy_A_uniq) if bledy_A_uniq else 'TODO'}")
print(f"  Błędy B:                {sorted(bledy_B_uniq) if bledy_B_uniq else 'TODO'}")
print(f"  Wspólne:                {sorted(wspolne) if wspolne else 'TODO'}")
print(f"  Tylko w A:              {sorted(tylko_A) if tylko_A else 'TODO'}")
print(f"  Łącznie unikalnych:     {liczba_unikalnych or 'TODO'}")
print(f"  B ma unikalne (vs A):   {B_ma_unikalne if B_ma_unikalne is not None else 'TODO'}")

print()

# =============================================================
# ZADANIE 2c: Inwersja słownika z grupowaniem
# =============================================================
# Masz słownik ocen studentów. Odwróć go tak, by
# klucz = ocena (int), wartość = lista studentów z tą oceną.

oceny_studentow = {
    "Anna": 5, "Bartek": 4, "Celina": 5, "Damian": 3,
    "Ewa": 4, "Filip": 2, "Grażyna": 5, "Hanna": 3
}

def odwroc_slownik(slownik):
    odwrocony = {}

    for imie, ocena in slownik.items():
        odwrocony.setdefault(ocena, []).append(imie)

    return odwrocony


print("Inwersja słownika ocen:")
wynik2 = odwroc_slownik(oceny_studentow)
if wynik2:
    for ocena in sorted(wynik2, reverse=True):
        print(f"  Ocena {ocena}: {sorted(wynik2[ocena])}")