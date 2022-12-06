from bs4 import BeautifulSoup
import re
from idm import downIDM
from recaptcha_bypass import pass_captcha
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import os, sys, time,requests

url = "https://gogoanime.run/category/detective-conan"

r = requests.get(url, allow_redirects=True)

soup = BeautifulSoup(r.text, 'html.parser')

new_eps = soup.select(".tab")[-1].select(".name")

def num_from_str(string):
    return int(re.findall(r'\b\d+\b', string)[0])

exist_ep = [num_from_str(ep) for ep in os.listdir("E:/Videos/Videos/Anime/Detective Conan")]

non_exist_ep = ["https://gogoanime.run"+ep.parent.get("href") for ep in new_eps if num_from_str(ep.getText()) not in exist_ep]

down_links =[]
for ep in non_exist_ep:
    try:
        r_ep = requests.get(ep, allow_redirects=True)

        soup_ep = BeautifulSoup(r_ep.text, 'html.parser')
        down = soup_ep.find("li", class_="dowloads")
        down_link = down.find_next("a").get("href")
        down_links.append((" ".join(soup_ep.find("h1").getText().split()[:4]), down_link))
    
    except:
        print(ep[0], " Anon FHD Link not found")

fhd_links = []

option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
option.add_argument("headless")
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
browser = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=option)

for link in down_links:
    try:
        r = requests.get(link[1], allow_redirects=True)
        browser.get(r.url)
        time.sleep(5)
        pass_captcha(browser)
        time.sleep(2)

        fhd_link = browser.find_element(By.PARTIAL_LINK_TEXT, "1080P").get_dom_attribute("href")
        
        fhd_links.append((link[0], fhd_link))
        time.sleep(10) 
    except:
        print(link[0], "FHD Link is not working")

print(fhd_links)

for link in fhd_links:
    try:
        os.mkdir("E:/Videos/Videos/Anime/Detective Conan")
    except:
        pass

    if not os.path.exists("E:/Videos/Videos/Anime/Detective Conan"+"/"+link[0]):
        # r_link = requests.get(link[1], allow_redirects=True)
        path = "E:/Videos/Videos/Anime/Detective Conan"
        downIDM(link[1], path, link[0] )

    # open("E:/Videos/Videos/Anime/"+link[0]+"/"+link[1].split("/")[-1], "wb").write(r_link.content)
