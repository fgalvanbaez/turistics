# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import shared_task
from bs4 import BeautifulSoup
from web.models import Host
import requests
from web import scraper

@shared_task
def request_tripadvisor():
    scraper.scrap_tripadvisor()



