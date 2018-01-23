from datetime import datetime
from Menu import Menu

def main():
    menu = Menu()
    matchesBase = []
    baseStart, baseEnd = menu.readSavedData(matchesBase)

    matches = []
    print("Ustaw zakres dat do analizy")
    menu.getDates()
    baseStart, baseEnd = menu.downloadMatches(matches, matchesBase, baseStart, baseEnd)
    print("Mecze w zakresie: {}".format(len(matches)))

    filteredMatches = matches
    filterKeys = []
    filterValues = []

    while True:
        print("\nMozesz wyswietlic mecze, zmienic zakres dat lub dodac/usunac filtry")
        print("Opcje:\n'w' - wyswiet wyniki\n'z' - zmien zakres dat\n'f' - dodaj filtr\n'u' - usun filtr\n'q' - zakoncz")
        while True:
            chosenOption = input("Wybrana opcja: ")
            if (chosenOption.lower() == "w" or chosenOption.lower() == "f" or chosenOption.lower() == "u" or chosenOption.lower() == "z" or chosenOption.lower() == "q"):
                break
            else:
                print("Bledny wybor. Sprobuj ponownie")

        if (chosenOption.lower() == "w"):
            for match in filteredMatches:
                match.printMatchRow()

        elif (chosenOption.lower() == 'z'):
            print("Ustaw zakres dat do analizy")
            menu.getDates()
            baseStart, baseEnd = menu.downloadMatches(matches,matchesBase, baseStart, baseEnd)
            print("Mecze w zakresie: {}".format(len(matches)))

        elif (chosenOption.lower() == 'q'):
            break

        elif chosenOption.lower() == 'f':
            print("Wybierz kategorie filtra")
            print("'l' - liga\n'd' - druzyna")
            while True:
                filterType = input("Wybrana opcja: ")
                if filterType.lower() == "l" or filterType.lower() == "d":
                    break
                else:
                    print("Bledny wybor. Sprobuj ponownie")

            filterExpr = input("Podaj filtrowane wyrazenie: ")

            filterKeys.append(filterType)
            filterValues.append(filterExpr)

            filteredMatches = menu.filterMatches(matches, filterKeys, filterValues)



    # longestTeam = menu.longestTeam(matches)
    # print(longestTeam)

if __name__ == "__main__":
    main()
