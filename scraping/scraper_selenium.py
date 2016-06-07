# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from web.models import Host
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os


chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver_firefox = webdriver.Firefox()
#driver_chrome = webdriver.Chrome(chromedriver)
# driver = webdriver.Firefox()
#url = "https://www.tripadvisor.es"

def scrap_tripadvisor(link):

    try:
        driver_firefox.get(link)
        i = 1
        list_hoteles = driver_firefox.find_element_by_id('ACCOM_OVERVIEW')

        hotels_n = list_hoteles.find_elements_by_class_name('listing')

        # Elimino el hotel patrocinado
        if len(hotels_n) > 30:
            hotels_n.pop(0)


        print len(hotels_n)
        for h in hotels_n:
            try:
                hotel = h.find_element_by_class_name('property_title')
                name = hotel.text
                print hotel.text + "  ------  " + str(i)
                code = hotel.get_attribute('id')
                # print code
                total = h.find_element_by_class_name('sprite-ratings').get_attribute('alt')
                rate = total.split(' ')

                ranking = h.find_element_by_class_name('slim_ranking').text
                print ranking


                #link =  hotel.get_attribute('href')
                #print link


                """host = Host.objects.create(type='H', code=code, name=name, total=rate[0])
                host.save()"""

                i += 1

            except Exception as e:
                print e

    except Exception as e:
        print e


    #Recogida de datos para hostales
    try:

        driver_firefox.get(link)
        BB = driver_firefox.find_element_by_xpath('//*[@id="p13n_PROPTYPE_BOX"]/div/div[2]/div/a')

        print BB.get_attribute('href')

        driver_firefox.get(BB.get_attribute('href'))

        i = 1
        list_BB = driver_firefox.find_element_by_id('ACCOM_OVERVIEW')
        BB_n = list_BB.find_elements_by_class_name('listing')

        # Elimino el hotel patrocinado
        if len(BB_n) > 30:
            BB_n.pop(0)

        print len(BB_n)
        for b in BB_n:
            try:
                bb = b.find_element_by_class_name('property_title')
                name = bb.text
                print name + "  ------  " + str(i)
                code = bb.get_attribute('id')
                # print code
                total = b.find_element_by_class_name('sprite-ratings').get_attribute('alt')
                rate = total.split(' ')

                ranking = b.find_element_by_class_name('slim_ranking').text
                print ranking

                """host = Host.objects.create(type='B', code=code, name=name, total=rate[0])
                host.save()"""

                i += 1

            except Exception as e:
                print e


    except Exception as e:
        print e
        print "Zona BB"

    # Recogida de datos para Otros
    try:

        driver_firefox.get(link)
        others = driver_firefox.find_element_by_xpath('//*[@id="p13n_PROPTYPE_BOX"]/div/div[3]/div/a')

        print others.get_attribute('href')

        driver_firefox.get(others.get_attribute('href'))

        i = 1
        list_others = driver_firefox.find_element_by_id('ACCOM_OVERVIEW')
        others_n = list_others.find_elements_by_class_name('listing')

        # Elimino el hotel patrocinado
        if len(others_n) > 30:
            others_n.pop(0)

        print len(others_n)
        for o in others_n:
            try:
                other = o.find_element_by_class_name('property_title')
                name = other.text
                print name + "  ------  " + str(i)
                code = other.get_attribute('id')
                # print code
                total = o.find_element_by_class_name('sprite-ratings').get_attribute('alt')
                rate = total.split(' ')

                ranking = o.find_element_by_class_name('slim_ranking').text
                print ranking

                """host = Host.objects.create(type='O', code=code, name=name, total=rate[0])
                host.save()"""

                i += 1

            except Exception as e:
                print e


    except Exception as e:
        print e
        print "Zona Others"


    driver_firefox.close()