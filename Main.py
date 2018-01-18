from Menu import Menu

def main():
    menu = Menu()
    matches = []
    print("Ustaw zakres dat do analizy")
    menu.getDates()
    menu.downloadMatches(matches)
    print("Mecze w zakresie: {}".format(len(matches)))

    filteredMatches = matches

    while True:
        print("Mozesz wyswietlic mecze, zmienic zakres dat lub dodac/usunac filtry")
        print("Wpisz 'w' zeby wyswietlic, 'z' zeby zmenic zakres dat, 'f' zeby dodac filtr, 'u' zeby usunac filtr, lub 'q' zeby zakonczyc")
        while True:
            chosenOption = input("Wybrana opcja ['w','z','f','u','q']: ")
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
            menu.downloadMatches(matches)
            print("Mecze w zakresie: {}".format(len(matches)))
        elif (chosenOption.lower() == 'q'):
            break


    # longestTeam = menu.longestTeam(matches)
    # print(longestTeam)



if __name__ == "__main__":
    main()