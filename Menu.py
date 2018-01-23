from datetime import timedelta, datetime
from ScrapPage import scrapPage
from Match import Match
import csv

class Menu:

    startDate = datetime.today()
    endDate = datetime.today()
    today = datetime.today()

    def readSavedData(self, matches):
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
                    match.predScore1 = (row[11], row[12])
                    match.predScore2 = (row[13], row[14])
                    match.predUnder = row[15]
                    match.predOver = row[16]
                    match.matchScore = (row[17], row[18])
                    matches.append(match)
                rownum += 1

            file.close()
            print("Wczytano {} meczow z bazy".format(rownum - 1))
            return baseStart, baseEnd

        except FileNotFoundError:
            print("Nie znaleziono pliku z baza meczow, bedzie stworzona nowa baza")
            file = open("baza.csv", "w", newline='')
            writer = csv.writer(file)
            writer.writerow([baseStart.strftime("%d %m %Y"), baseEnd.strftime("%d %m %Y")])
            file.close()
            baseStart = datetime.today()
            baseEnd = datetime.today()
            return baseStart, baseEnd

    def getDates(self):
        while True:
            try:
                self.startDate = datetime.strptime(input("Data poczatkowa [dd mm rrrr]: "), "%d %m %Y")
                if self.startDate.date() < self.today.date():
                    break
                else:
                    print("Podaj wczesniejsza date")
            except ValueError:
                print("Zly format daty. Sprobuj ponownie")
        while True:
            try:
                self.endDate = datetime.strptime(input("Data koncowa [dd mm rrrr]: "), "%d %m %Y")
                if self.endDate.date() < self.today.date():
                    if self.endDate.date() >= self.startDate.date():
                        break
                    else:
                        print("Data koncowa musi byc pozniejsza, lub rowna poczatkowej")
                else:
                    print("Podaj wczesniejsza date")
            except ValueError:
                print("Zly format daty. Sprobuj ponownie")

    def setDatesRange(self, date1, date2):
        tempList = []
        for n in range(int((date2 - date1).days)+1):
            tempList.append(date1 + timedelta(n))
        return tempList

    def downloadMatches(self, matches, matchesBase, baseStart, baseEnd):
        matches.clear()
        baseDateList = self.setDatesRange(baseStart, baseEnd)
        tempDateList = self.setDatesRange(self.startDate, self.endDate)
        splitDateList = []

        if baseEnd.date() == self.today.date():
            if baseStart.date() == self.today.date():
                baseEnd = self.endDate
        elif self.endDate.date() > baseEnd.date():
            if self.startDate.date() > baseEnd.date():
                splitDateList = self.setDatesRange(baseEnd + timedelta(1), self.startDate - timedelta(1))
            baseEnd = self.endDate
        if self.startDate.date() < baseStart.date():
            if self.endDate.date() < baseStart.date():
                splitDateList = self.setDatesRange(self.endDate + timedelta(1), baseStart - timedelta(1))
            baseStart = self.startDate

        file = open("baza.csv", "a", newline='')

        for date in tempDateList:
            if date not in baseDateList:
                scrapPage(date, matchesBase, file)

        for date in splitDateList:
            scrapPage(date,matchesBase, file)

        file.close()
        file = open("baza.csv", "r+", newline='')
        file.write(baseStart.strftime("%d %m %Y") + "," + baseEnd.strftime("%d %m %Y"))
        file.close()

        copyList = []
        for date in tempDateList:
            copyList.append(date.date())
        for x in matchesBase:
            if x.timeStart.date() in copyList:
                matches.append(x)

        return baseStart, baseEnd

    def filterMatches(self, matches, filterKeys, filterValues):
        filteredMatches = []
        nFilters = len(filterKeys)
        for n in range(nFilters):
            if filterKeys[n] == "l":
                for match in matches:
                    if match.league == filterValues[n]:
                        if match not in filteredMatches:
                            filteredMatches.append(match)
            elif filterKeys[n] == "d":
                for match in matches:
                    if match.homeTeam == filterValues[n] or match.awayTeam == filterValues[n]:
                        if match not in filteredMatches:
                            filteredMatches.append(match)
        return filteredMatches

    def displayCorrectMatches(self, matches):
        counter = 0
        for match in matches:
            if match.predIsCorrect():
                match.printMatchRow()
                counter = counter + 1
        print(counter)

    def longestTeam(self, matches):
        longestTeam = 0
        for match in matches:
            longestTeam = max(len(match.homeTeam), len(match.awayTeam), longestTeam)
        return longestTeam