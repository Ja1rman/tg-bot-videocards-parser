# -*- coding: utf-8 -*-

import telebot
import requests
import traceback
import multiprocessing as mp
import time
import random
from bs4 import BeautifulSoup
import discord_webhook

bot = telebot.TeleBot('1680508706:AAGu_zrjj1X9BzYMNUhb3CW1E7ABey4Ft8Q')
CHANNEL = '@nvidiart'

proxies = ["https://MiSyCcnd:qVgHXfYS@45.138.147.177:53094",
           "https://MiSyCcnd:qVgHXfYS@92.249.12.59:52850",
           "https://MiSyCcnd:qVgHXfYS@45.139.52.158:46229",
           "https://MiSyCcnd:qVgHXfYS@176.103.91.220:64742"]

wb1 = 'https://discord.com/api/webhooks/814066453115830293/Xk74QP0cuPMl5_AtBYQ5e1mdkbd4_EejaNiyFFKwQ43uzi6P7p1iJKrvcC2_kmKrMwWH'
wb2 = 'https://discord.com/api/webhooks/814040297503588392/W2afc48KHL2Ds92p_TvMK5xITPEPBMWPSXg292sKDF5JpA5xz7NlK1J0TcjSP3p7k9t4'

def ogo():
    while True:
        for id in range(60, 91, 10):
            try:
                url = 'https://ogo1.ru/search/?only_available=Y&q=rtx%2030' + \
                    str(id)
                response = requests.get(url, headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find_all(
                    "div", {"class": "js-b-catalog-plates__item category-page__row-col js-item"})
                for product in soup:
                    try:
                        pricet = product.find(
                            "div", {"class": "b-plate-product__price"}).get_text()
                        price = ''
                        for ch in pricet:
                            if ch.isdigit():
                                price += ch
                        price = int(price)
                        if id == 60 and price < 65000 or id == 70 and price < 75000 or id == 80 and price < 100000 or id == 90 and price < 150000:
                            href = product.find(
                                "a", {"class": "js-b-plate-product__caption-text js-b-list-product__caption-text"})['href']
                            bot.send_message(
                                CHANNEL, 'https://ogo1.ru' + href, disable_web_page_preview=True)
                            discord_webhook.DiscordWebhook(url=wb1,
                                                           content='https://ogo1.ru' + href).execute()
                            discord_webhook.DiscordWebhook(url=wb2,
                                                           content='https://ogo1.ru' + href).execute()
                    except: print(traceback.format_exc())
            except: print(traceback.format_exc())


def onlineTrade():
    while True:
        for id in range(60, 91, 10):
            try:
                response = requests.get('https://www.onlinetrade.ru/sitesearch.html?query=rtx+30' + str(id) + '&sort=price-asc&page=0&page=0', headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find_all('div', {'class': 'indexGoods__item'})
                for product in soup[0:10]:
                    try:
                        try:
                            free = product.find(
                                "a", {"class": "button button__orange js__ajaxExchange"}).get_text()
                        except:
                            continue
                        pricet = product.find(
                            "span", {"class": "price regular"}).get_text()
                        price = ''
                        for ch in pricet:
                            if ch.isdigit():
                                price += ch
                        price = int(price)
                        if price > 30000 and (id == 60 and price < 65000 or id == 70 and price < 75000 or id == 80 and price < 100000 or id == 90 and price < 150000):
                            href = product.find(
                                "a", {"class": "indexGoods__item__image"})['href']
                            bot.send_message(
                                CHANNEL, 'https://www.onlinetrade.ru' + href, disable_web_page_preview=True)
                            discord_webhook.DiscordWebhook(url=wb1,
                                                           content='https://www.onlinetrade.ru' + href).execute()
                            discord_webhook.DiscordWebhook(url=wb2,
                                                           content='https://www.onlinetrade.ru' + href).execute()
                    except: print(traceback.format_exc())
            except: print(traceback.format_exc())


aliUrls = ['https://aliexpress.ru/item/1005001837109821.html',
           'https://aliexpress.ru/item/1005001671921502.html',
           'https://aliexpress.ru/item/1005001671979254.html',
           'https://aliexpress.ru/item/1005001671841809.html']


def aliexpress(url):
    while True:
        try:
            response = requests.get(url, headers={
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
            quant = response.text
            quant = quant[quant.find('totalAvailQuantity')+20:]
            quant = quant[:quant.find('}')]
            if quant != '0' and response.status_code == 200:
                bot.send_message(CHANNEL, url, disable_web_page_preview=True)
                discord_webhook.DiscordWebhook(url=wb1,
                                                content=url).execute()
                discord_webhook.DiscordWebhook(url=wb2,
                                                content=url).execute()
        except: print(traceback.format_exc())

def oldi():
    while True:
        for id in range(60, 91, 10):
            try:
                url = 'https://sort.diginetica.net/search?st=rtx%2030' + str(id) + '&apiKey=4OC8353048&strategy=vectors_extended,zero_queries_predictor&fullData=true&withCorrection=true&withFacets=true&treeFacets=true&regionId=&useCategoryPrediction=true&size=24&offset=0&showUnavailable=false&unavailableMultiplier=0.2&preview=false&withSku=false&sort=PRICE_DESC'
                response = requests.get(url, headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}, proxies={'https': proxies[0]})
                for product in response.json()['products']:
                    price = float(product['price'])
                    if price > 25000 and (price < 65000 and id == 60 or price < 75000 and id == 70 or price < 100000 and id == 80 or price < 150000 and id == 90) and product['categories'][0]['name'] == 'Видеокарты':
                        bot.send_message(CHANNEL, 'https://www.oldi.ru/catalog/element/' + product['id'], disable_web_page_preview=True)
                        discord_webhook.DiscordWebhook(url=wb1,
                                                content='https://www.oldi.ru/catalog/element/' + product['id']).execute()
                        discord_webhook.DiscordWebhook(url=wb2,
                                                content='https://www.oldi.ru/catalog/element/' + product['id']).execute()
            except: print(traceback.format_exc())

def vk():
    lastText = ''
    while True:
        try:
            response = requests.get('https://vk.com/nvidia', headers={
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
            soup = BeautifulSoup(response.text, 'html.parser')
            soup = soup.find('div', {
                             'class': '_post post page_block all own post--with-likes closed_comments deep_active'})
            text = soup.find('div', {'class': 'wall_post_text'}).get_text()
            if ('vk.cc' in text.lower() or 'aliexpress' in text.lower()) and text != lastText:
                bot.send_message(CHANNEL, text, disable_web_page_preview=True)
                discord_webhook.DiscordWebhook(url=wb1,
                                                content=text).execute()
                discord_webhook.DiscordWebhook(url=wb2,
                                                content=text).execute()
                lastText = text
        except: print(traceback.format_exc())

if __name__ == "__main__":
    threads = []

    threads.append(mp.Process(target=ogo))
    threads[-1].start()

    threads.append(mp.Process(target=onlineTrade))
    threads[-1].start()

    for url in aliUrls:
        threads.append(mp.Process(target=aliexpress, args=(url,)))
        threads[-1].start()

    threads.append(mp.Process(target=vk))
    threads[-1].start()

    threads.append(mp.Process(target=oldi))
    threads[-1].start()
