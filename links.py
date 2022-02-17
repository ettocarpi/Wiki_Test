from bs4 import BeautifulSoup as bs
import requests
import json
import csv

#res = requests.get("https://en.wikipedia.org/wiki/List_of_naval_battles")
res = requests.get("https://it.wikipedia.org/wiki/Fisica")
soup = bs(res.text, "html.parser")
links = {}
for link in soup.find_all("a"):
    url = link.get("href", "")
    # if "/wiki/Battle" in url:
    #     links[link.text.strip()] = url
    links[link.text.strip()] = url

print(links)

json_links = json.dumps(links)

# with open("links.json",'w',encoding="utf-8") as jsonfile:
#     jsonfile.write(json_links)

links_columns = ['','']
with open("links.csv",'w',encoding="utf-8") as csvfile:
    for key in links.keys():
        csvfile.write("%s, %s\n" % (key, links[key]))