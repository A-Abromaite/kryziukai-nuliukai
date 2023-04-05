lenta = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
uzimtos_pozicijos = []
zaidejo_X_laimejimai = 0
zaidejo_0_laimejimai = 0


def piesiam_lenta():
    print(f"{lenta[0]} | {lenta[1]} | {lenta[2]}")
    print("_________")
    print(f"{lenta[3]} | {lenta[4]} | {lenta[5]}")
    print("_________")
    print(f"{lenta[6]} | {lenta[7]} | {lenta[8]}")


def laimejimas():
    laiminti_kombinacija = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for kombinacija in laiminti_kombinacija:
        if lenta[kombinacija[0]] == lenta[kombinacija[1]] == lenta[kombinacija[2]]:
            return True
    return False


def lygiosios():
    for i in lenta:
        if i.isdigit() and i != "0":
            return False
    return True


def zaidimas():
    global zaidejo_X_laimejimai, zaidejo_0_laimejimai
    zaidejas = "X"
    while True:
        piesiam_lenta()
        pozicija = input(f"Žaidėjau {zaidejas}, pasirinkite laisvą poziciją nuo 1 iki 9: ")
        while pozicija not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or int(pozicija) - 1 in uzimtos_pozicijos:
            pozicija = input("Netinkama įvestis. Pasirinkite laisvą poziciją: ")
        pozicija = int(pozicija) - 1
        if zaidejas == "X":
            lenta[pozicija] = "X"
            uzimtos_pozicijos.append(pozicija)
        else:
            lenta[pozicija] = "0"
            uzimtos_pozicijos.append(pozicija)
        if laimejimas():
            piesiam_lenta()
            if zaidejas == "X":
                zaidejo_X_laimejimai += 1
                print(
                    f"Žaidėjas {zaidejas} laimėjo žaidimą! Rezultatas yra {zaidejo_X_laimejimai}:{zaidejo_0_laimejimai}")
            else:
                zaidejo_0_laimejimai += 1
                print(
                    f"Žaidėjas {zaidejas} laimėjo žaidimą! Rezultatas yra {zaidejo_X_laimejimai}:{zaidejo_0_laimejimai}")
            break
        if lygiosios():
            piesiam_lenta()
            print(f"Lygiosios! Rezultatas yra {zaidejo_X_laimejimai}:{zaidejo_0_laimejimai}")
            break
        if zaidejas == "X":
            zaidejas = "0"
        else:
            zaidejas = "X"


while True:
    zaidimas()
    pasirinkimas = input("Ar norite kartori žaidimą? (Įveskite T/N): ").capitalize()
    while pasirinkimas not in ["T", "N"]:
        pasirinkimas = input("Netinkama įvestis. Ar norite kartori žaidimą? (Įveskite T/N): ").capitalize()
    if pasirinkimas == "T":
        lenta = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        uzimtos_pozicijos = []
    else:
        if pasirinkimas == "N":
            print("Viso gero")
            break
