import pywintypes
import win32clipboard
import pyperclip as pc
import keyboard
import os, time
import pyautogui as pya
from f2a import f2a
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
option.add_argument("headless")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
browser = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=option)


yamli_url ="https://www.yamli.com/arabic-keyboard/"

browser.get(yamli_url)



def get_selected_text():
    time.sleep(0.2)
    pya.hotkey('ctrl', 'c')
    time.sleep(0.01)
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text

def paste_new_text(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    pya.hotkey('ctrl', 'v')


keyboard.add_hotkey('ctrl+shift+a', lambda: paste_new_text(f2a(browser, get_selected_text())))

keyboard.wait()