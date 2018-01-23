from datetime import datetime
from Menu import Menu
from Match import Match
import csv

def main():
    matchesBase = []
    baseStart = datetime.today()
    baseEnd = datetime.today()
    baseStart, baseEnd = readSavedData(matchesBase, baseStart, baseEnd)

    matches = []
    menu = Menu()
    print("Ustaw zakres dat do analizy")
    menu.getDates()
    baseStart, baseEnd = menu.downloadMatches(matches, matchesBase, baseStart, baseEnd)
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
            baseStart, baseEnd = menu.downloadMatches(matches,matchesBase, baseStart, baseEnd)
            print("Mecze w zakresie: {}".format(len(matches)))
        elif (chosenOption.lower() == 'q'):
            break
        #elif chosenOption.lower() == 'f':



    # longestTeam = menu.longestTeam(matches)
    # print(longestTeam)

def readSavedData(matches, baseStart, baseEnd):
    try:
        file = open("baza.csv", "r", newline='')
        reader = csv.reader(file)
        rownum = 0

        for row in reader:
            if rownum == 0:
                baseStart = datetime.strptime(row[0], "%d %m %Y")
                baseEnd = datetime.strptime(row[1], "%d %m %Y")
            else:
                match = Match()
                match.league = row[0]
                match.timeStart = datetime.strptime(row[1], "%d %m %Y %H:%M")
                match.homeTeam = row[2]
                match.awayTeam = row[3]
                match.predProbHome = row[4]
                match.predProbDraw = row[5]
                match.predProbAway = row[6]
                match.predTips = row[7]
                match.oddsHome = row[8]
                match.oddsDraw = row[9]
                match.oddsAway = row[10]
                match.predScore1 = (row[11],row[12])
                match.predScore2 = (row[13],row[14])
                match.predUnder = row[15]
                match.predOver = row[16]
                match.matchScore = (row[17],row[18])
                matches.append(match)
            rownum += 1

        file.close()
        print("Wczytano {} meczow z bazy".format(rownum-1))
        return baseStart, baseEnd

    except FileNotFoundError:
        print("Nie znaleziono pliku z baza meczow, bedzie stworzona nowa baza")
        file = open("baza.csv", "w", newline='')
        writer = csv.writer(file)
        writer.writerow([baseStart.strftime("%d %m %Y"), baseEnd.strftime("%d %m %Y")])
        file.close()
        return baseStart, baseEnd

if __name__ == "__main__":
    main()
