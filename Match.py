from time import localtime, strftime

class Match:

    def __init__(self):
        self.league = ""
        self.timeStart = strftime("%H:%M", localtime())
        self.homeTeam = ""
        self.awayTeam = ""
        self.predProbHome = 0
        self.predProbDraw = 0
        self.predProbAway = 0
        self.predTips = 0
        self.oddsHome = 0.00
        self.oddsDraw = 0.00
        self.oddsAway = 0.00
        self.predScore1 = 0, 0
        self.predScore2 = 0, 0
        self.predUnder = 0
        self.predOver = 0
        self.matchScore = 0, 0

    def predIsCorrect(self):
        if self.predScore1 == self.matchScore or self.predScore2 == self.matchScore:
            return True
        else:
            return False

    def printMatchRow(self):
        print("{} {}: {:18} - {:18} {}".format(strftime("%d %m %Y %H:%M", self.timeStart), self.league,self.homeTeam,self.awayTeam, self.matchScore))