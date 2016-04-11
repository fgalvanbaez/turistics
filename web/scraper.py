# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#from web.models import Host

import requests

def scrap_tripadvisor():

    #url = raw_input("Enter a website to extract the URL's from: ")
    #domain of web to request
    domain = "https://www.tripadvisor.es"

    #hotels
    tenerife = "/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"  #Pasar por parámetro desde task con celery

    try:
        req = requests.get(domain + tenerife)
    except Exception as e:
        print e

    data = req.text
    soup = BeautifulSoup(data, "html.parser")

    #Hoteles de Tenerife
    for link in soup.find_all('a'):

        s = str(link.get("href"))
        if ("Hotel_Review" in s > 0) and ("#REVIEWS" in s > 0):

            #print (link.get('href'))
            req2 = requests.get(domain + link.get('href'))
            hotel = req2.text
            soup2 = BeautifulSoup(hotel, "html.parser")
            text = soup2.find("h1", id="HEADING")

            #Aquí obtengo el nombre del alojamiento
            name = text.get_text().replace("\n", '')  #Reemplazo los salto de página del html

            text = soup2.find("div", id="SUMMARYBOX")
            scores = []

            for l in text.find_all("li"):
                score = l.span.img.attrs['alt'].split()[0]
                scores.append(score)

            print (name)
            for i in scores:
                print i

            #host = Host.objects.create(type='H', name=name, sleep_quality=scores[0], location=scores[1], rooms=scores[2],
                                       #services=scores[3], quality_price=scores[4], cleaning=scores[5])


