import requests
from bs4 import BeautifulSoup
import re
from idm import downIDM
import os

url = "https://anime4up.tv/"

r = requests.get(url, allow_redirects=True)

soup = BeautifulSoup(r.text, 'html.parser')

new_eps = soup.select(".ep-card-anime-title a")

followed_animes = ["Mairimashita! Iruma-kun 3rd Season", "Spy x Family Part 2", "Shinobi no Ittoki", "Xian Wang de Richang Shenghuo 3", "Mob Psycho 100 III", "Bleach: Sennen Kessen-hen", "Boku no Hero Academia 6th Season", "Yowamushi Pedal: Limit Break", "Detective Conan"]

new_eps_filtered = [(ep.getText() , ep.parent.parent.parent.find("a").get("href")) for ep in new_eps if ep.getText() in followed_animes]

fhd_links =[]
for ep in new_eps_filtered:
    r_ep = requests.get(ep[1], allow_redirects=True)

    soup_ep = BeautifulSoup(r_ep.text, 'html.parser')
    fhd = soup_ep.find("li", string=re.compile("FHD"))
    fhd_link = fhd.find_next("a", string=re.compile("anonfiles")).get("href")
    fhd_links.append((ep[0], fhd_link))

down_links = []
for link in fhd_links:
    r_link = requests.get(link[1], allow_redirects=True)

    soup_link = BeautifulSoup(r_link.text, 'html.parser')

    down_link = soup_link.find(id = "download-url").get("href")
    down_links.append((link[0], down_link))
    print(down_link.split("/")[-1])

for link in down_links:
    # r_link = requests.get(link[1], allow_redirects=True)
    folder = link[0].replace(":","")
    try:
        os.mkdir("E:/Videos/Videos/Anime/"+folder)
    except:
        pass

    if not os.path.exists("E:/Videos/Videos/Anime/"+folder+"/"+link[1].split("/")[-1]):
        path = os.path.join("E:/Videos/Videos/Anime/", folder)
        downIDM(link[1], path, link[1].split("/")[-1] )

    # open("E:/Videos/Videos/Anime/"+link[0]+"/"+link[1].split("/")[-1], "wb").write(r_link.content)
