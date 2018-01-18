from datetime import timedelta, datetime
from ScrapPage import scrapPage

class Menu:

    startDate = datetime.today()
    endDate = datetime.today()
    datesList = []

    def getDates(self):
        while True:
            try:
                self.startDate = datetime.strptime(input("Data poczatkowa [dd mm rrrr]: "), "%d %m %Y")
                break
            except ValueError:
                print("Zly format daty. Sprobuj ponownie")
        while True:
            try:
                self.endDate = datetime.strptime(input("Data koncowa [dd mm rrrr]: "), "%d %m %Y")
                break
            except ValueError:
                print("Zly format daty. Sprobuj ponownie")

    def setDatesRange(self, date1, date2):
        tempList = []
        for n in range(int((date2 - date1).days)+1):
            tempList.append(date1 + timedelta(n))
        return tempList

    def downloadMatches(self,matches):
        tempDateList = self.setDatesRange(self.startDate, self.endDate)
        for date in tempDateList:
            if date not in self.datesList:
                scrapPage(date, matches)
        removeList = []
        for date in self.datesList:
            if date not in tempDateList:
                for x in matches:
                    if x.timeStart.date() == date.date():
                        removeList.append(x)
        for x in removeList:
            matches.remove(x)
        self.datesList = tempDateList

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