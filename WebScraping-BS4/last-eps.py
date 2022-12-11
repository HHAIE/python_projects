import requests
from bs4 import BeautifulSoup
import re
from idm import downIDM
import os


def down_last_eps(followed_animes):
    url = "https://anime4up.tv/"

    r = requests.get(url, allow_redirects=True)

    soup = BeautifulSoup(r.text, 'html.parser')

    new_eps = soup.select(".ep-card-anime-title a")
    def num_from_str(string):
        return int(re.findall(r'\b\d+\b', string)[0])

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

        name = folder+ " Episode " + str(num_from_str(link[1].split("/")[-1])) + " [Arabic] " + link[1].split("/")[-1][-4:]
        if not os.path.exists("E:/Videos/Videos/Anime/"+folder+"/"+name):
            path = "E:/Videos/Videos/Anime/"+folder
            downIDM(link[1], path, name)

