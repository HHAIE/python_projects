import requests
from bs4 import BeautifulSoup
import re
from idm import downIDM
import os


def down_eps_an4up(url, name, eps_count):
    r = requests.get(url, allow_redirects=True)

    soup = BeautifulSoup(r.text, 'html.parser')

    new_eps = soup.select("#DivEpisodesList")

    try:
        os.mkdir("E:/Videos/Videos/Anime/"+name)
    except:
        pass

    def num_from_str(string):
        return int(re.findall(r'\b\d+\b', string)[0])
    exist_ep = [num_from_str(ep) for ep in os.listdir("E:/Videos/Videos/Anime/"+name)]

    last_eps = [(ep.find_previous_sibling("img").get("alt"), ep.get("href")) for ep in new_eps[0].find_all("a", class_="overlay") if num_from_str(ep.find_previous_sibling("img").get("alt")) not in exist_ep][-1*eps_count:]

    fhd_links =[]
    for ep in last_eps:
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
        ep_name = name+ " Episode " + str(num_from_str(link[1].split("/")[-1])) + " [Arabic] " + link[1].split("/")[-1][-4:]
        if not os.path.exists("E:/Videos/Videos/Anime/"+name+"/"+ep_name):
            path = "E:/Videos/Videos/Anime/"+name
            downIDM(link[1], path, ep_name)

