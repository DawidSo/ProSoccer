from lxml import html
import requests
from Match import Match
from datetime import datetime

def scrapPage(date, matches):
    url = "http://www.prosoccer.gr/en/{}/{:02d}/soccer-predictions-{}-{:02d}-{:02d}.html".format(date.year, date.month, date.year, date.month, date.day)
    dateStr = "{:02d} {:02d} {} ".format(date.day, date.month, date.year)

    page = requests.get(url)
    tree = html.fromstring(page.content)

    count_elements = tree.xpath('count(//*[@id="tblPredictions"]/tbody/tr)')
    print("Dodano {:02.0f} meczow".format(count_elements))

    for matchElement in tree.xpath('//*[@id="tblPredictions"]/tbody/tr'):
        match = Match()
        match.league = matchElement.xpath('td[1]')[0].text_content()
        time = matchElement.xpath('td[2]')[0].text_content()
        match.timeStart = datetime.strptime(dateStr + time, "%d %m %Y %H:%M")
        tempTeams = matchElement.xpath('td[3]')[0].text_content()
        match.homeTeam = tempTeams[0:tempTeams.find("-") - 1]
        match.awayTeam = tempTeams[tempTeams.find("-") + 2:len(tempTeams)]
        match.predProbHome = matchElement.xpath('td[4]')[0].text_content()
        match.predProbDraw = matchElement.xpath('td[5]')[0].text_content()
        match.predProbAway = matchElement.xpath('td[6]')[0].text_content()
        match.predTips = matchElement.xpath('td[7]')[0].text_content()
        match.oddsHome = matchElement.xpath('td[8]')[0].text_content()
        match.oddsDraw = matchElement.xpath('td[9]')[0].text_content()
        match.oddsAway = matchElement.xpath('td[10]')[0].text_content()
        tempScore = matchElement.xpath('td[11]')[0].text_content()
        match.predScore1 = tempScore[0:tempScore.find("-")], tempScore[tempScore.find("-") + 1:len(tempScore)]
        tempScore = matchElement.xpath('td[12]')[0].text_content()
        match.predScore2 = tempScore[0:tempScore.find("-")], tempScore[tempScore.find("-") + 1:len(tempScore)]
        match.predUnder = matchElement.xpath('td[13]')[0].text_content()
        match.predOver = matchElement.xpath('td[14]')[0].text_content()
        tempScore = matchElement.xpath('td[15]')[0].text_content()
        match.matchScore = tempScore[0:tempScore.find("-") - 1], tempScore[tempScore.find("-") + 2:len(tempScore)]
        matches.append(match)


# page = requests.get('http://www.prosoccer.gr/en/2018/01/soccer-predictions-2018-01-14.html')
#
# tree = html.fromstring(page.content)
#
# count_elements = tree.xpath('count(//*[@id="tblPredictions"]/tbody/tr)')
# print(count_elements)
#
#
# for matchElement in tree.xpath('//*[@id="tblPredictions"]/tbody/tr'):
#     match = Match()
#     match.league = matchElement.xpath('td[1]')[0].text_content()
#     time = matchElement.xpath('td[2]')[0].text_content()
#     match.timeStart = strptime(date + time, "%d %m %Y %H:%M")
#     tempTeams = matchElement.xpath('td[3]')[0].text_content()
#     match.homeTeam = tempTeams[0:tempTeams.find("-")-1]
#     match.awayTeam = tempTeams[tempTeams.find("-")+2:len(tempTeams)]
#     match.predProbHome = matchElement.xpath('td[4]')[0].text_content()
#     match.predProbDraw = matchElement.xpath('td[5]')[0].text_content()
#     match.predProbAway = matchElement.xpath('td[6]')[0].text_content()
#     match.predTips = matchElement.xpath('td[7]')[0].text_content()
#     match.oddsHome = matchElement.xpath('td[8]')[0].text_content()
#     match.oddsDraw = matchElement.xpath('td[9]')[0].text_content()
#     match.oddsAway = matchElement.xpath('td[10]')[0].text_content()
#     tempScore = matchElement.xpath('td[11]')[0].text_content()
#     match.predScore1 = tempScore[0:tempScore.find("-")], tempScore[tempScore.find("-")+1:len(tempScore)]
#     tempScore = matchElement.xpath('td[12]')[0].text_content()
#     match.predScore2 = tempScore[0:tempScore.find("-")], tempScore[tempScore.find("-")+1:len(tempScore)]
#     match.predUnder = matchElement.xpath('td[13]')[0].text_content()
#     match.predOver = matchElement.xpath('td[14]')[0].text_content()
#     tempScore = matchElement.xpath('td[15]')[0].text_content()
#     match.matchScore = tempScore[0:tempScore.find("-")-1], tempScore[tempScore.find("-")+2:len(tempScore)]
#     matches.append(match)
