from datetime import timedelta, datetime
from ScrapPage import scrapPage

class Menu:

    startDate = datetime.today()
    endDate = datetime.today()
    today = datetime.today()

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

        if baseEnd.date() == self.today.date():
            if baseStart.date() == self.today.date():
                baseEnd = self.endDate
        elif self.endDate.date() > baseEnd.date():
            baseEnd = self.endDate
        if self.startDate.date() < baseStart.date():
            baseStart = self.startDate

        file = open("baza.csv", "a", newline='')

        for date in tempDateList:
            if date not in baseDateList:
                scrapPage(date, matchesBase, file)

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

        # removeList = []
        # for date in self.datesList:
        #     if date not in tempDateList:
        #         for x in matches:
        #             if x.timeStart.date() == date.date():
        #                 removeList.append(x)
        # if len(removeList) > 0:
        #     print("Usunieto {} meczow".format(len(removeList)))
        # for x in removeList:
        #     matches.remove(x)
        # for date in tempDateList:
        #     if date not in self.datesList:
        #         scrapPage(date, matches)
        # self.datesList = tempDateList

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