"""
Ćwiczenie 1 — Instrukcje warunkowe
Czas: ~10 minut
"""

# =============================================================
# ZADANIE 1a: Kalkulator BMI
# =============================================================
# Napisz funkcję oblicz_bmi(waga_kg, wzrost_m) która:
# - Oblicza wskaźnik BMI: waga / (wzrost ** 2)
# - Na podstawie wyniku zwraca KROTKĘ (bmi, kategoria):
#   < 18.5  → "Niedowaga"
#   18.5–24.99 → "Waga prawidłowa"
#   25–29.99   → "Nadwaga"
#   >= 30      → "Otyłość"
# - Obsługuje błędne dane: wzrost <= 0 lub waga <= 0 → zwraca (None, "Błąd danych")

def oblicz_bmi(waga_kg, wzrost_m):
    if wzrost_m <=0 or waga_kg <= 0:
        return (None, "Błąd danych")

    bmi = waga_kg / (wzrost_m ** 2)  

    if bmi < 18.5:
        return (bmi, "Niedowaga")
    elif 18.5 <= bmi < 25:
        return (bmi, "Waga prawidłowa")
    elif 25 <= bmi < 30:
        return (bmi, "Nadwaga")
    elif bmi >= 30:
        return (bmi, "Otyłość")
    pass


# Testy (uruchom, aby sprawdzić):
przypadki = [
    (70, 1.75),    # oczekiwane: ~22.9, Waga prawidłowa
    (50, 1.70),    # oczekiwane: ~17.3, Niedowaga
    (90, 1.75),    # oczekiwane: ~29.4, Nadwaga
    (120, 1.70),   # oczekiwane: ~41.5, Otyłość
    (70, 0),       # oczekiwane: (None, "Błąd danych")
    (-5, 1.75),    # oczekiwane: (None, "Błąd danych")
]
print("Test oblicz_bmi:")
for waga, wzrost in przypadki:
    wynik = oblicz_bmi(waga, wzrost)
    bmi, kat = wynik if wynik else (None, None)
    bmi_str = f"{bmi:.1f}" if bmi else "N/A"
    print(f"  waga={waga}, wzrost={wzrost} → {bmi_str} ({kat})")

print()

# =============================================================
# ZADANIE 1b: Klasyfikator trójkąta
# =============================================================
# Napisz funkcję klasyfikuj_trojkat(a, b, c) która:
# - Sprawdza, czy podane boki tworzą trójkąt (warunek trójkąta)
# - Jeśli tak, klasyfikuje go:
#   a == b == c         → "równoboczny"
#   a == b lub b == c lub a == c → "równoramienny"
#   a²+b²==c² (lub permutacje) → "prostokątny"
#   wpp → "różnoboczny"
# - Jeśli nie tworzą trójkąta → zwraca "nie trójkąt"
# WSKAZÓWKA: Posortuj boki przed sprawdzaniem prostokątności
import math

def klasyfikuj_trojkat(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0) or not (a < b + c and b < a + c and c < a + b):
        return "nie trójkąt"
    
    # Sprawdzenie warunku trójkąta
    if a == b == c:
        return "równoboczny"
    elif a == b or b == c or a == c:
        return "równoramienny"
    elif math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
        return "prostokątny"
    else:
        return "różnoboczny"
    pass


print("Test klasyfikuj_trojkat:")
przypadki_t = [
    (3, 3, 3),     # równoboczny
    (5, 5, 8),     # równoramienny
    (3, 4, 5),     # prostokątny
    (5, 7, 9),     # różnoboczny
    (1, 2, 10),    # nie trójkąt
]
for a, b, c in przypadki_t:
    wynik = klasyfikuj_trojkat(a, b, c)
    print(f"  ({a}, {b}, {c}) → {wynik}")