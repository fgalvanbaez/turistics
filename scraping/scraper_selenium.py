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
        hotels_n = driver_firefox.find_elements_by_class_name('listing')

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

                """host = Host.objects.create(type='H', code=code, name=name, sleep_quality=1, location=1, rooms=1,
                    services=1, quality_price=1, cleaning=1, total=rate[0])

                host.save()"""

                i += 1

            except Exception as e:
                print e

        next = driver_firefox.find_element_by_class_name("next")

        pag = 1
        while next is not None:

            pag += 1
            driver_firefox.get(next.get_attribute('href'))
            hotels_n = driver_firefox.find_elements_by_class_name('listing_info')


            #Elimino el hotel patrocinado
            if len(hotels_n) > 30:
                hotels_n.pop(0)

            print len(hotels_n)

            for h in hotels_n:
                driver_firefox.implicitly_wait(10)
                try:
                    hotel = h.find_element_by_class_name('property_title')
                    i += 1
                    name = hotel.text
                    code = hotel.get_attribute('id')

                    try:
                        total = h.find_element_by_class_name('sprite-ratings').get_attribute('alt')
                    except Exception as e:
                        print e

                    try:
                        rate = total.split(' ')
                    except Exception as e:
                        print e

                    try:
                        ranking = h.find_element_by_class_name('slim_ranking').text
                    except Exception as e:
                        print e

                    """host = Host.objects.create(type='H', code=code, name=name, sleep_quality=1, location=1, rooms=1,
                        services=1, quality_price=1, cleaning=1, total=rate[0])

                    host.save()"""

                    print name + "  ------  " + str(i)
                    print code
                    print rate[0]
                    print ranking

                except Exception as e:

                    i += 1
                    print e
                    print "Estoy en el while capullo"

            try:
                next = driver_firefox.find_element_by_class_name("next")

                if "disable" in next.get_attribute('class'):
                    next = None

            except Exception as e:
                print e
                print "Estoy fuera del while"

            print "*********************" + str(pag)

    except Exception as e:
        print e
        print "Estoy saliendo del primer try"

    driver_firefox.close()