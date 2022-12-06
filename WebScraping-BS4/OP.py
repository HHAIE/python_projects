import requests
from bs4 import BeautifulSoup
import re
from idm import downIDM
import os

url = "https://anime4up.tv/anime/one-piece/"

r = requests.get(url, allow_redirects=True)

soup = BeautifulSoup(r.text, 'html.parser')

new_eps = soup.select("#DivEpisodesList")

def num_from_str(string):
    return int(re.findall(r'\b\d+\b', string)[0])
exist_ep = [num_from_str(ep) for ep in os.listdir("E:/Videos/Videos/Anime/One Piece")]

last_ep30 = [(ep.find_previous_sibling("img").get("alt"), ep.get("href")) for ep in new_eps[0].find_all("a", class_="overlay") if num_from_str(ep.find_previous_sibling("img").get("alt")) not in exist_ep][-30:]

fhd_links =[]
for ep in last_ep30:
    try:
        r_ep = requests.get(ep[1], allow_redirects=True)

        soup_ep = BeautifulSoup(r_ep.text, 'html.parser')
        fhd = soup_ep.find("li", string=re.compile("FHD"))
        fhd_link = fhd.find_next("a", string=re.compile("anonfiles")).get("href")
        fhd_links.append((ep[0], fhd_link))
    
    except:
        print(ep[0], " Anon FHD Link not found")


down_links = []
for link in fhd_links:
    try:
        r_link = requests.get(link[1], allow_redirects=True)

        soup_link = BeautifulSoup(r_link.text, 'html.parser')

        down_link = soup_link.find(id = "download-url").get("href")
        down_links.append((link[0], down_link))

    except:
        print(link[0], " Anon FHD Link is not working")

for link in down_links:
    try:
        os.mkdir("E:/Videos/Videos/Anime/One Piece")
    except:
        pass

    if not os.path.exists("E:/Videos/Videos/Anime/One Piece"+"/"+link[1].split("/")[-1]):
        path = "E:/Videos/Videos/Anime/One Piece"
        name = "One Piece Episode " + str(num_from_str(link[1].split("/")[-1])) + " [Arabic]" + link[1].split("/")[-1][-4:]
        downIDM(link[1], path, name)

