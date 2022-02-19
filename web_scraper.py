from email import header
from bs4 import BeautifulSoup
import requests as req

#Bestand openen met daarin alle URL's.
file = open('websites.txt', 'r')
lines = file.readlines()

#Logbestanden bijhouden.
scrapableSites = open("scrapable.txt", "w+")
nietGevondenSites = open("notfound.txt", 'w+')

#User agent gaat de requests sturen naar de sites.
useragent = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0'}


#Alle sites doornemen.
for site in lines:
    adres = 'http://' + site.strip()
    
    
    try:
        #Soup maken en page ophalen.
        page = req.get(adres, headers=useragent, timeout=10)
        soup = BeautifulSoup(page.text, 'html.parser')


        #Alle P-tags ophalen
        gold = "".join([p.text for p in soup.find_all('p')])
        #print(gold)

        

        #Alle mails van de site ophalen.
        mailtos = soup.select('a[href^=mailto]')
        for mail in mailtos:
            mailadres = mail.get_text()
            #print(mailadres)


        #Alle telefoonnummers van de site ophalen.
        data = soup.html.findAll('p')
        for tag in data:
            tagSearch = str(tag)
            if '+32' in tagSearch:
                print(tag.get_text())
        



        #Indien gelukt, print adres uit en log deze site bij de scrapable sites.
        print(f'V - {adres}')

        scrapableSites.write(f'{adres}\n')

    except:
        #Indien het niet gelukt is om de site op te halen -- vb timeout -- log dit.
        print(f'X - {adres}')
        nietGevondenSites.write(f'{adres}\n')


#Logbestanden finaliseren.
scrapableSites.close()
nietGevondenSites.close()