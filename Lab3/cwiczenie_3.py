"""
Ćwiczenie 3 — Zakres zmiennych (scope)
Czas: ~15 minut
"""

# =============================================================
# ZADANIE 3a: Analiza zakresu — przewidywanie wyników
# =============================================================
# Dla KAŻDEGO fragmentu kodu NAJPIERW zapisz w komentarzu
# co Twoim zdaniem zostanie wydrukowane, a POTEM uruchom i sprawdź.

# --- Fragment 1 ---
x = 100


def zmien_x():
    x = 200
    print(f"  wewnątrz: x = {x}")


zmien_x()
print(f"  na zewnątrz: x = {x}")
# TWOJA PRZEWIDYWANIE: wewnątrz = ???, na zewnątrz = ???

print()

# --- Fragment 2 ---
lista = [1, 2, 3]


def dodaj_do_listy():
    lista.append(4)


dodaj_do_listy()
print(f"  lista po wywołaniu: {lista}")
# TWOJA PRZEWIDYWANIE: lista = ???

print()

# --- Fragment 3 ---
y = 10


def zewnetrzna():
    y = 20

    def wewnetrzna():
        print(f"  wewnetrzna: y = {y}")

    wewnetrzna()
    print(f"  zewnetrzna: y = {y}")


zewnetrzna()
print(f"  globalna: y = {y}")
# TWOJA PRZEWIDYWANIE: wewnetrzna = ???, zewnetrzna = ???, globalna = ???

print()

# --- Fragment 4 (PUŁAPKA!) ---
# Odkomentuj poniższy kod i przewidź co się stanie:
#
# z = 50
# def pulapka():
#     print(z)    # Co się stanie?
#     z = 100
#
# pulapka()
# TWOJA PRZEWIDYWANIE: ???

print("=== Zadanie 3a: Odpowiedzi powyżej ===")
print()

# =============================================================
# ZADANIE 3b: Licznik z domknięciem (closure)
# =============================================================
# Napisz funkcję stworz_licznik(start=0, krok=1) która:
# - Zwraca FUNKCJĘ (domknięcie/closure)
# - Każde wywołanie zwróconej funkcji zwiększa wewnętrzny
#   licznik o 'krok' i zwraca aktualną wartość
# - Użyj 'nonlocal' do modyfikacji zmiennej z zakresu nadrzędnego
#
# Przykład:
#   licz = stworz_licznik(10, 5)
#   licz() → 15
#   licz() → 20
#   licz() → 25


def stworz_licznik(start=0, krok=1):
    # TODO: Uzupełnij — użyj nonlocal
    pass


print("=== Zadanie 3b: Licznik z domknięciem ===")
if stworz_licznik() is not None:
    licz_a = stworz_licznik()  # start=0, krok=1
    licz_b = stworz_licznik(100, 10)  # start=100, krok=10

    print("  Licznik A (0, +1):", [licz_a() for _ in range(5)])  # [1, 2, 3, 4, 5]
    print(
        "  Licznik B (100, +10):", [licz_b() for _ in range(5)]
    )  # [110, 120, 130, 140, 150]
else:
    print("  TODO: Zaimplementuj stworz_licznik()")

print()

# =============================================================
# ZADANIE 3c: Akumulator z historią
# =============================================================
# Napisz funkcję stworz_akumulator() która zwraca SŁOWNIK
# z trzema funkcjami:
#   "dodaj"    — dodaje wartość do sumy i zapisuje w historii
#   "suma"     — zwraca aktualną sumę
#   "historia" — zwraca listę wszystkich dodanych wartości
#   "cofnij"   — cofa ostatnią operację (usuwa z historii i odejmuje od sumy)
#
# Wszystkie funkcje operują na WSPÓLNYCH zmiennych (closure/nonlocal).
#
# Przykład:
#   akum = stworz_akumulator()
#   akum["dodaj"](10)  → 10
#   akum["dodaj"](20)  → 30
#   akum["historia"]() → [10, 20]
#   akum["cofnij"]()   → 10
#   akum["historia"]() → [10]


def stworz_akumulator():
    # TODO: Uzupełnij — wspólne zmienne + nonlocal
    pass


print("=== Zadanie 3c: Akumulator z historią ===")
akum = stworz_akumulator()
if akum is not None:
    print(f"  dodaj(10): {akum['dodaj'](10)}")  # 10
    print(f"  dodaj(20): {akum['dodaj'](20)}")  # 30
    print(f"  dodaj(5):  {akum['dodaj'](5)}")  # 35
    print(f"  historia:  {akum['historia']()}")  # [10, 20, 5]
    print(f"  suma:      {akum['suma']()}")  # 35
    print(f"  cofnij:    {akum['cofnij']()}")  # 30
    print(f"  historia:  {akum['historia']()}")  # [10, 20]
else:
    print("  TODO: Zaimplementuj stworz_akumulator()")
