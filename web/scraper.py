# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from web.models import Host

import requests


def scrap_tripadvisor(link):

    try:
        req = requests.get(link)
    except Exception as e:
        print e

    data = req.text
    soup = BeautifulSoup(data, "html.parser")


    #Hoteles de Tenerife
    for link in soup.find_all('a'):

        domain = "https://www.tripadvisor.es"
        s = str(link.get("href"))
        if ("Hotel_Review" in s > 0) and ("#REVIEWS" in s > 0):


            #print (link.get('href'))
            req2 = requests.get(domain + s)
            hotel = req2.text
            soup2 = BeautifulSoup(hotel, "html.parser")

            # Aquí obtengo el nombre del alojamiento
            text = soup2.find("h1", id="HEADING")
            name = text.get_text().replace("\n", '')  #Reemplazo los salto de página del html


            rate = soup2.find('img', property="ratingValue")
            print rate['content']
            rateTotal = rate['content'].replace(".", ",")
            rateTotal
            print rateTotal

            #Obtención del tipo de alojamiento
            secondary_navbar = soup2.find('ul', id='BREADCRUMBS')

            #Usado para eliminar los saltos de línea en el array contents
            for i in secondary_navbar.contents:
                if i == '\n':
                    secondary_navbar.contents.remove(i)

            print len(secondary_navbar.contents)
            print secondary_navbar.contents[len(secondary_navbar.contents)-1].contents[0].contents[0].string

            type = ''
            if "Hoteles" in secondary_navbar.contents[len(secondary_navbar.contents)-1].contents[0].contents[0].string:
                type = 'H'

            if "B&B" in secondary_navbar.contents[len(secondary_navbar.contents)-1].contents[0].contents[0].string:
                type = 'B'

            if "Alquiler vacacional" in secondary_navbar.contents[len(secondary_navbar.contents) - 1].contents[0].contents[0].string:
                type = 'A'

            if "Otros" in secondary_navbar.contents[len(secondary_navbar.contents) - 1].contents[0].contents[0].string:
                type = 'O'


            host = Host.objects.create(type=type, name=name, sleep_quality=1, location=1, rooms=1,
                                       services=1, quality_price=1, cleaning=1, total=rateTotal)

            host.save()
