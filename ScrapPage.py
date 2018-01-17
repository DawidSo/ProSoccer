from lxml import html
import requests
from Match import Match
from time import strptime

# page = requests.get('http://www.prosoccer.gr/en/2018/01/soccer-predictions-2018-01-01.html')
page = requests.get('http://www.prosoccer.gr/en/2018/01/soccer-predictions-2018-01-14.html')

tree = html.fromstring(page.content)

count_elements = tree.xpath('count(//*[@id="tblPredictions"]/tbody/tr)')
print(count_elements)

matches = []

for matchElement in tree.xpath('//*[@id="tblPredictions"]/tbody/tr'):
    match = Match()
    match.league = matchElement.xpath('td[1]')[0].text_content()
    time = matchElement.xpath('td[2]')[0].text_content()
    match.timeStart = strptime(time, "%H:%M")
    tempTeams = matchElement.xpath('td[3]')[0].text_content()
    match.homeTeam = tempTeams[0:tempTeams.find("-")-1]
    match.awayTeam = tempTeams[tempTeams.find("-")+2:len(tempTeams)]
    match.predProbHome = matchElement.xpath('td[4]')[0].text_content()
    match.predProbDraw = matchElement.xpath('td[5]')[0].text_content()
    match.predProbAway = matchElement.xpath('td[6]')[0].text_content()
    match.predTips = matchElement.xpath('td[7]')[0].text_content()
    match.oddsHome = matchElement.xpath('td[8]')[0].text_content()
    match.oddsDraw = matchElement.xpath('td[9]')[0].text_content()
    match.oddsAway = matchElement.xpath('td[10]')[0].text_content()
    tempScore = matchElement.xpath('td[11]')[0].text_content()
    match.predScore1 = tempScore[0:tempScore.find("-")], tempScore[tempScore.find("-")+1:len(tempScore)]
    tempScore = matchElement.xpath('td[12]')[0].text_content()
    match.predScore2 = tempScore[0:tempScore.find("-")], tempScore[tempScore.find("-")+1:len(tempScore)]
    match.predUnder = matchElement.xpath('td[13]')[0].text_content()
    match.predOver = matchElement.xpath('td[14]')[0].text_content()
    tempScore = matchElement.xpath('td[15]')[0].text_content()
    match.matchScore = tempScore[0:tempScore.find("-")-1], tempScore[tempScore.find("-")+2:len(tempScore)]
    matches.append(match)

counter = 0
print(matches[1].predScore1)
for match in matches:
    if match.predIsCorrect():
        print(f"{match.homeTeam} - {match.awayTeam}")
        counter = counter + 1
print(counter)
