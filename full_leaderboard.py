import requests
from bs4 import BeautifulSoup
import time
import random

year = 2022
points = dict()
for day in range(1, 26):
    url = "https://adventofcode.com/{}/leaderboard/day/{}".format(year, day)
    r = requests.get(url)
    if r.status_code == 404:
        print("No content for day {}".format(day))
        break

    print("Parsing day {}...".format(day))
    soup = BeautifulSoup(BeautifulSoup(r.content, 'html5lib').prettify(), 'html5lib')

    entries = soup.findAll("div", {"class": "leaderboard-entry"})
    for entry in entries:
        pos = int(entry.find("span", {"class": "leaderboard-position"}).contents[0].strip()[:-1])
        name = entry.find("span", {"class": "leaderboard-userphoto"}).next_sibling.strip()
        if len(name) <= 0:
            name = entry.find("span", {"class": "leaderboard-anon"}).contents[0].strip()
        points[name] = points.get(name, 0) + (101 - pos)

    time.sleep(max(0.5, 2 + random.gauss(0, 0.5)))

s_keys = sorted(points, key=points.get, reverse=True)
place = 0
point = 0
count = 1
print("\n\n====================")
print("Leaderboard")
print("====================")
for key in s_keys:
    if not point == points[key]:
        place += count
        count = 1
    else:
        count += 1
    point = points[key]
    print("{}) {} -- {}".format(place, points[key], key))
