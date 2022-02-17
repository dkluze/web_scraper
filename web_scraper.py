from bs4 import BeautifulSoup
import requests as req

file = open('websites.txt', 'r')
lines = file.readlines()

for site in lines:
    adres = 'http://' + site.strip()
    try:
        page = req.get(adres)
        soup = BeautifulSoup(page.text, 'html.parser')
        gold = "".join([p.text for p in soup.find_all('p')])
        print(adres)
    except:
        print(f'{adres} niet beschikbaar')