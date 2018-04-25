#Inividual Homework 5 Bonus
#Spbooth
#Group 54

import urllib.request
import re

url = "http://www.cbssports.com/nfl/scoreboard/all/2016/regular/5/"
web_page = urllib.request.urlopen(url)
contents = web_page.read().decode(errors="replace")
web_page.close()
body = re.findall('(?<=<body).+(?=</body>)', contents, re.DOTALL)[0]
headingTag = re.findall('(?<=<h[1-9]>).+?(?=</h[1-9]>)', body)
for tag in headingTag:
    print("The heading tag on this page is:", tag)
imageLinks = re.findall('(?<=<img src=").+(?=" class="logo")', body)
print("A list of links to all the logo images on the page:")#, imageLinks)
for link in imageLinks:
    print(link)

tables = re.findall('(?<=<tbody).+?(?=</tbody>)', contents, re.DOTALL)
games = re.findall('(?<=<td class="total-score").+?(?=</td>)', contents, re.DOTALL)
print("There were", int(len(games)/2), "games played this week")
for i in range(len(games)):
    games[i] = games[i][1:]
scores = []    
for i in range(len(games)//2):
    score1 = games.pop()
    score2 = games.pop()
    scoreDif = abs(int(score1)-int(score2))
    scores.append(scoreDif)
print("The greatest points difference this week was", max(scores), "points")
