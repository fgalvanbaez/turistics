# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from web.models import Host
from selenium import webdriver
import os
import requests

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver_firefox = webdriver.Firefox()
#driver_chrome = webdriver.Chrome(chromedriver)
# driver = webdriver.Firefox()
#url = "https://www.tripadvisor.es"

driver_firefox.implicitly_wait(10)


def scrap_tripadvisor(link):

    try:
        driver_firefox.get(link)
        next = driver_firefox.find_element_by_class_name("next")

        print len(next.get_attribute('href'))
        while len(next.get_attribute('href')) > 0:

            hotels_n = driver_firefox.find_elements_by_class_name('listing')
            for h in hotels_n:
                try:
                    hotel = h.find_element_by_class_name('property_title')

                    name = hotel.text
                    print hotel.text

                    code = hotel.get_attribute('id')
                    print code

                    total = h.find_element_by_class_name('sprite-ratings').get_attribute('alt')
                    rate = total.split(' ')

                    """host = Host.objects.create(type='H', code=code, name=name, sleep_quality=1, location=1, rooms=1,
                        services=1, quality_price=1, cleaning=1, total=rate[0])

                    host.save()"""

                except Exception as e:
                    print e

            print next.get_attribute('href')
            try:
                driver_firefox.get(next.get_attribute('href'))
                #driver_firefox.implicitly_wait(5)
            except Exception as e:
                print e

    except Exception as e:
        print e

    driver_firefox.close()