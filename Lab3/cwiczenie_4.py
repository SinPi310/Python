"""
Ćwiczenie 4 — Dobre praktyki i refaktoryzacja
Czas: ~15 minut
"""

# =============================================================
# ZADANIE 4a: Refaktoryzacja — early return
# =============================================================
# Poniższa funkcja działa poprawnie, ale jest trudna do czytania
# przez głębokie zagnieżdżenie. Przepisz ją używając wzorca
# "early return" (wczesne wyjście przy błędach).


# ORYGINAŁ — NIE ZMIENIAJ:
def przetworz_platnosc_oryginal(dane):
    if dane is not None:
        if "kwota" in dane:
            if dane["kwota"] > 0:
                if "waluta" in dane:
                    if dane["waluta"] in ("PLN", "EUR", "USD"):
                        if "klient_id" in dane:
                            return f"OK: {dane['kwota']} {dane['waluta']} dla klienta {dane['klient_id']}"
                        else:
                            return "Błąd: brak klient_id"
                    else:
                        return f"Błąd: nieobsługiwana waluta {dane['waluta']}"
                else:
                    return "Błąd: brak waluty"
            else:
                return "Błąd: kwota musi być dodatnia"
        else:
            return "Błąd: brak kwoty"
    else:
        return "Błąd: brak danych"


# TODO: Przepisz z early return — płaska struktura, max 1 poziom zagnieżdżenia
def przetworz_platnosc(dane):
    pass


# Testy (wyniki muszą być identyczne jak oryginał):
print("=== Zadanie 4a: Early return ===")
przypadki = [
    None,
    {},
    {"kwota": -50},
    {"kwota": 100},
    {"kwota": 100, "waluta": "GBP"},
    {"kwota": 100, "waluta": "PLN"},
    {"kwota": 250, "waluta": "EUR", "klient_id": 42},
]
for dane in przypadki:
    oryginal = przetworz_platnosc_oryginal(dane)
    nowa = przetworz_platnosc(dane)
    status = "✅" if oryginal == nowa else "❌"
    print(f"  {status} {str(dane):55s} → {nowa}")

print()

# =============================================================
# ZADANIE 4b: Refaktoryzacja — SRP (Single Responsibility)
# =============================================================
# Poniższa funkcja robi za dużo: waliduje, przelicza, formatuje
# i drukuje. Rozdziel ją na 4 OSOBNE funkcje.


# ORYGINAŁ — NIE ZMIENIAJ:
def raport_wynagrodzen_oryginal(pracownicy):
    """Przyjmuje listę dict: [{"imie": ..., "stawka": ..., "godziny": ...}]"""
    print("=== RAPORT WYNAGRODZEŃ ===")
    for p in pracownicy:
        if p["stawka"] <= 0 or p["godziny"] < 0:
            print(f"  {p['imie']}: BŁĄD DANYCH")
            continue
        wynagrodzenie = p["stawka"] * p["godziny"]
        if p["godziny"] > 160:
            nadgodziny = p["godziny"] - 160
            wynagrodzenie += nadgodziny * p["stawka"] * 0.5  # +50% za nadgodziny
        podatek = wynagrodzenie * 0.18
        netto = wynagrodzenie - podatek
        print(
            f"  {p['imie']}: brutto={wynagrodzenie:.2f}, podatek={podatek:.2f}, netto={netto:.2f}"
        )


# TODO: Rozdziel na osobne funkcje
def waliduj_pracownika(pracownik):
    """Zwraca True jeśli dane są poprawne, False jeśli nie."""
    # TODO
    pass


def oblicz_wynagrodzenie(stawka, godziny):
    """Oblicza wynagrodzenie brutto (z nadgodzinami)."""
    # TODO
    pass


def oblicz_podatek(brutto, stawka_podatku=0.18):
    """Oblicza podatek."""
    # TODO
    pass


def formatuj_raport(imie, brutto, podatek, netto):
    """Zwraca sformatowany string z danymi pracownika."""
    # TODO
    pass


def raport_wynagrodzen(pracownicy):
    """Generuje raport używając powyższych funkcji."""
    # TODO: Użyj waliduj, oblicz_wynagrodzenie, oblicz_podatek, formatuj_raport
    pass


print("=== Zadanie 4b: Refaktoryzacja SRP ===")
pracownicy = [
    {"imie": "Anna", "stawka": 50, "godziny": 160},
    {"imie": "Bartek", "stawka": 40, "godziny": 180},  # nadgodziny
    {"imie": "Celina", "stawka": -10, "godziny": 160},  # błąd
    {"imie": "Damian", "stawka": 60, "godziny": 120},
]

print("\nOryginał:")
raport_wynagrodzen_oryginal(pracownicy)
print("\nRefaktoryzacja:")
raport_wynagrodzen(pracownicy)

print()

# =============================================================
# ZADANIE 4c: Type hints i docstring
# =============================================================
# Poniższe funkcje działają, ale nie mają type hints ani docstringów.
# Dodaj:
# 1. Type hints do parametrów i wartości zwracanej
# 2. Docstring w formacie Google (Args, Returns)


def szukaj_w_tekscie(tekst, fraza, wielkosc_liter):
    pozycje = []
    if not wielkosc_liter:
        tekst = tekst.lower()
        fraza = fraza.lower()
    start = 0
    while True:
        pos = tekst.find(fraza, start)
        if pos == -1:
            break
        pozycje.append(pos)
        start = pos + 1
    return pozycje


def policz_slowa(tekst):
    slowa = tekst.split()
    wynik = {}
    for slowo in slowa:
        slowo = slowo.lower().strip(".,!?;:")
        wynik[slowo] = wynik.get(slowo, 0) + 1
    return wynik


print("=== Zadanie 4c: Type hints ===")
print(f"  szukaj: {szukaj_w_tekscie('Ala ma Ala kota', 'ala', False)}")
print(f"  słowa:  {policz_slowa('Ala ma kota. Kota ma Ala.')}")
print("  (Dodaj type hints i docstringi do powyższych funkcji)")
