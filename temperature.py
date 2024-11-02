import requests
from bs4 import BeautifulSoup

from core_utils import speak

def check_temperature():
    search = "temperature in Bhubaneswar"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"Current {search} is {temp}")
    print(f"Current {search} is {temp}")

