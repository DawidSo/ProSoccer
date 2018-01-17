from datetime import datetime
from Menu import Menu

def main():
    menu = Menu()
    print("Ustaw zakres dat do analizy")
    while True:
        try:
            menu.startDate = datetime.strptime(input("Data poczatkowa [dd mm rrrr]: "), "%d %m %Y")
            break
        except ValueError:
            print("Zly format daty. Sprobuj ponownie")
    while True:
        try:
            menu.endDate = datetime.strptime(input("Data koncowa [dd mm rrrr]: "), "%d %m %Y")
            break
        except ValueError:
            print("Zly format daty. Sprobuj ponownie")
    matches = menu.downloadMatches()

    print("Razem dodano {} meczow".format(len(matches)))
    # longestTeam = menu.longestTeam(matches)
    # print(longestTeam)

    for match in matches:
        match.printMatchRow()

if __name__ == "__main__":
    main()