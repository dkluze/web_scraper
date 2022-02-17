from bs4 import BeautifulSoup as bs
import requests as req
import pandas

provincies = ['Oost-Vl', 'West-Vl', 'Antwerpen', 'Limburg',  'Vl-Brabant']

f = open("websites.txt", "w+")

for prov in provincies:
    file = prov + '.csv'
    df = pandas.read_csv(file)
    lijst = df["Web adres"].tolist()
    
    for rij in lijst:
        if isinstance(rij, str) and rij.startswith('www') :
            f.write(rij + "\n")

