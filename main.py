# -*- coding: utf-8 -*-

import telebot
import requests
import time
import traceback
import threading
from discord_webhook import DiscordWebhook

ozonUrls = ["https://www.ozon.ru/context/detail/id/207702519/",
        "https://www.ozon.ru/context/detail/id/207702520/", 
        "https://www.ozon.ru/context/detail/id/216940493/",
        "https://www.ozon.ru/context/detail/id/178337786/",
        "https://www.ozon.ru/context/detail/id/173667655/",
        "https://www.ozon.ru/context/detail/id/178715781"]

def ozon(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text
            status = r[r.find('isAvailable')+13:]
            status = status[:status.find(',')]
            if status == 'true': DiscordWebhook(url='https://discord.com/api/webhooks/808402021770199120/6PWBz6hao8__SEL7pFhtJDjbAZ5hhJ6rLBJuvhGdMnlD3p8fKgSDfrkt92tkT6G6SyPQ', 
                                                content=url).execute()
        except: print(traceback.format_exc())

wildberriesUrls = ["https://www.wildberries.ru/catalog/15298664/detail.aspx",
                   "https://www.wildberries.ru/catalog/15298663/detail.aspx"]

def wildberries(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text
            status = r[r.find('isSoldOut"')+11:]
            status = status[:status.find(',')]
            if status == 'false': DiscordWebhook(url='https://discord.com/api/webhooks/808403407890415656/MvfMwly7JPdDjs3zRr_GF3mzGwxWPZEn6A5B9RaTla-8qBuzaaF25-UTzgx5bCQ3I5Fu', 
                                                content=url).execute()
        except: print(traceback.format_exc())

goodsUrls = ["https://goods.ru/catalog/details/igrovaya-pristavka-sony-playstation-5-825gb-100026864564",
             "https://goods.ru/catalog/details/igrovaya-pristavka-sony-playstation-5-digital-edition-100027598944"]

def goods(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text
            r = r[r.find('"skuCode":"' + url[url.rfind('-')+1:]):]
            status = r[r.find('availableShops')+16:]
            status = status[:status.find(',')]
            print(status)
            if status != '0': DiscordWebhook(url='https://discord.com/api/webhooks/808403718626082867/IYXICFI6L4oEbO2yNG-1Q4r9GxmJ21oODfF2qDFvaX9r8q-rHRpUmFUY-EA9xVAz3EaN', 
                                            content=url).execute()
        except: print(traceback.format_exc())

gameparkUrls = ["https://www.gamepark.ru/playstation5/console/IgrovayakonsolSonyPlayStation5/",
                "https://www.gamepark.ru/playstation5/console/IgrovayakonsolSonyPlayStation5DigitalEdition/"]

def gamepark(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            print(response.status_code)
            r = response.text
            if 'Нет в наличии' not in r: DiscordWebhook(url='https://discord.com/api/webhooks/808404192682180648/TKbq2iPcPN4DQkW05RKRl4cNcPeKDHVVpdAIwV6g7UD-ujj4NNJDHoJehK0tmZeYptJF', 
                                                        content=url).execute()
        except: print(traceback.format_exc())

if __name__ == "__main__":
    threads = []
    for i in range(len(ozonUrls)):
        threads.append(threading.Thread(target=(ozon), args=(ozonUrls[i],)))
        threads[-1].start()
    
    for i in range(len(wildberriesUrls)):
        threads.append(threading.Thread(target=(wildberries), args=(wildberriesUrls[i],)))
        threads[-1].start()

    for i in range(len(goodsUrls)):
        threads.append(threading.Thread(target=(goods), args=(goodsUrls[i],)))
        threads[-1].start()

    for i in range(len(gameparkUrls)):
        threads.append(threading.Thread(target=(gamepark), args=(gameparkUrls[i],)))
        threads[-1].start()
