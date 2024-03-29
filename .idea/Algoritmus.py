from Seznam import Seznam


# Algoritmus
def upraveny_seznam(seznam, pravidlo):
    index = 0
    while index < len(seznam):
        if not pravidlo(seznam[index]):
            del seznam[index]
        else:
            index += 1


# 1 Možnost: Sudá čísla
def pravidlo_suda_cisla(prvek):
    return prvek % 2 == 0


# 2 Možnost: lichá čísla
def pravidlo_licha_cisla(prvek):
    return prvek % 2 != 0


seznam = Seznam.generuj_seznam()

# Vstup uživatele
while True:
    volba = input("Vyberte možnost:"
                  "\n1) Zobraz pouze sudá čísla"
                  "\n2) Zobraz pouze lichá čísla"
                  "\n3) Ukončit"
                  "\nVolba: ")

    if volba == '1':
        upraveny_seznam(seznam, pravidlo_suda_cisla)
        print("Sudá čísla ze seznamu:", seznam)
    elif volba == '2':
        upraveny_seznam(seznam, pravidlo_licha_cisla)
        print("Lichá čísla ze seznamu:", seznam)
    elif volba == '3':
        print("Konec programu.")
        break
    else:
        print("Neplatná volba. Zadejte 1, 2 nebo 3.")
