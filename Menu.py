from datetime import timedelta, date
from ScrapPage import scrapPage

class Menu:

    startDate = date.today()
    endDate = date.today()

    def setDatesRange(self, date1, date2):
        for n in range(int((date2 - date1).days)+1):
            yield date1 + timedelta(n)

    def downloadMatches(self):
        matches= []
        for date in self.setDatesRange(self.startDate, self.endDate):
            scrapPage(date, matches)
        return matches

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