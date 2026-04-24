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