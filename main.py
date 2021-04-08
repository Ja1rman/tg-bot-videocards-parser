# -*- coding: utf-8 -*-

import telebot
import requests
import traceback
import multiprocessing as mp
import time
import random
from bs4 import BeautifulSoup
import discord_webhook
import re

bot = telebot.TeleBot('1680508706:AAGu_zrjj1X9BzYMNUhb3CW1E7ABey4Ft8Q')
CHANNEL = '@nvidiart'

proxies = ["https://MiSyCcnd:qVgHXfYS@45.138.147.177:53094",
           "https://MiSyCcnd:qVgHXfYS@92.249.12.59:52850",
           "https://MiSyCcnd:qVgHXfYS@45.139.52.158:46229",
           "https://MiSyCcnd:qVgHXfYS@176.103.91.220:64742"]

wb2 = 'https://discord.com/api/webhooks/814040297503588392/W2afc48KHL2Ds92p_TvMK5xITPEPBMWPSXg292sKDF5JpA5xz7NlK1J0TcjSP3p7k9t4'

def ogo():
    while True:
        models = ['2060', '3070', '3080', '3060', '3090']
        for model in models:
            try:
                url = 'https://ogo1.ru/search/?only_available=Y&q=rtx%20' + model
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
                        name = product.find(
                            "a", {"class": "js-b-plate-product__caption-text js-b-list-product__caption-text"}).get_text()
                        if price >= 30000 and ('2060' in name and price <= 50000 or '3060' in name and price <= 70000 or '3070' in name and price <= 100000 or '3080' in name and price <= 160000 or '3090' in name and price <= 190000):
                            href = product.find(
                                "a", {"class": "js-b-plate-product__caption-text js-b-list-product__caption-text"})['href']
                            bot.send_message(
                                CHANNEL, 'https://ogo1.ru' + href, disable_web_page_preview=True)
                            discord_webhook.DiscordWebhook(url=wb2,
                                                           content='https://ogo1.ru' + href).execute()
                    except: print(traceback.format_exc())
            except: print(traceback.format_exc())


def onlineTrade():
    while True:
        models = ['2060', '3070', '3080', '3060', '3090']
        for model in models:
            try:
                response = requests.get('https://www.onlinetrade.ru/sitesearch.html?query=rtx+' + model + '&sort=price-asc&page=0&page=0', headers={
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
                        if price >= 30000 and (model == '2060' and price <= 50000 or model == '3060' and price <= 70000 or model == '3070' and price <= 100000 or model == '3080' and price <= 160000 or model == '3090' and price <= 190000):
                            href = product.find(
                                "a", {"class": "indexGoods__item__image"})['href']
                            bot.send_message(
                                CHANNEL, 'https://www.onlinetrade.ru' + href, disable_web_page_preview=True)
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
                discord_webhook.DiscordWebhook(url=wb2,
                                                content=url).execute()
        except: print(traceback.format_exc())

def oldi():
    while True:
        models = ['2060', '3070', '3080', '3060', '3090']
        for model in models:
            try:
                url = 'https://sort.diginetica.net/search?st=rtx%20' + model + '&apiKey=4OC8353048&strategy=vectors_extended,zero_queries_predictor&fullData=true&withCorrection=true&withFacets=true&treeFacets=true&regionId=&useCategoryPrediction=true&size=24&offset=0&showUnavailable=false&unavailableMultiplier=0.2&preview=false&withSku=false&sort=PRICE_DESC'
                response = requests.get(url, headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
                for product in response.json()['products']:
                    price = float(product['price'])
                    if price >= 30000 and (model == '2060' and price <= 50000 or model == '3060' and price <= 70000 or model == '3070' and price <= 100000 or model == '3080' and price <= 160000 or model == '3090' and price <= 190000):
                        bot.send_message(CHANNEL, 'https://www.oldi.ru/catalog/element/' + product['id'], disable_web_page_preview=True)
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
                discord_webhook.DiscordWebhook(url=wb2,
                                                content=text).execute()
                lastText = text
        except: print(traceback.format_exc())

def regard():
    while True:
        models = ['2060', '3070', '3080', '3060', '3090']
        for model in models:
            try:
                url = 'https://www.regard.ru/catalog/?query=rtx%20' + model
                response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find_all('div', {'class': 'block'})
                for product in soup:
                    try:
                        pricet = product.find('div', {'class': 'price'}).get_text()
                        price = ''
                        for ch in pricet:
                            if ch.isdigit():
                                price += ch
                        price = int(price)
                        if price >= 30000 and (model == '2060' and price <= 50000 or model == '3060' and price <= 70000 or model == '3070' and price <= 100000 or model == '3080' and price <= 160000 or model == '3090' and price <= 190000):
                            href = product.find("div", {"class": "code"}).get_text()
                            href = href.replace('ID: ', '')
                            href = 'https://www.regard.ru/catalog/tovar' + href + '.htm'
                            bot.send_message(CHANNEL, href, disable_web_page_preview=True)
                            discord_webhook.DiscordWebhook(url=wb2,
                                                            content=href).execute()
                    except: print(traceback.format_exc())
            except: print(traceback.format_exc())

def dns():
    url = 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/?q='
    models = ['2060', '3070', '3080', '3060', '3090', '6700', '6800', '6900']
    while True:
        for model in models:
            try:
                response = requests.get(url + model, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find_all('a', {'class': 'catalog-product__name ui-link ui-link_black'})
                for href in soup:
                    try:
                        link = 'https://www.dns-shop.ru' + href['href']
                        response = requests.get(link, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
                        price = response.text
                        price = price[price.find('price":')+7:]
                        price = price[:price.find(',')]
                        price = int(price)
                        if price >= 30000 and (model == '2060' and price <= 50000 or model == '3060' and price <= 70000 or model == '3070' and price <= 100000 or model == '3080' and price <= 160000 or model == '3090' and price <= 190000 or model == '6700' and price <= 65000 or model == '6800' and price <= 100000 or model == '6900' and price <= 150000):
                            s = BeautifulSoup(response.text, 'html.parser')
                            s = s.find('h1', {'class': 'page-title product-card-top__title'})
                            if '6700' in s.get_text() or '6800' in s.get_text() or '6900' in s.get_text():
                                discord_webhook.DiscordWebhook(url='https://discord.com/api/webhooks/822164863404867654/He8zzdoOsbwWYwXcsfiMpuRPQyTF2Zug0FaYlOp2JBMUDn50ZaPsNNCLKdToIriTmGa4', content=link).execute()
                            elif '2060' in s.get_text() or '3060' in s.get_text() or '3070' in s.get_text() or '3070' in s.get_text() or '3080' in s.get_text() or '3090' in s.get_text():
                                discord_webhook.DiscordWebhook(url=wb2, content=link).execute()
                    except: print(traceback.format_exc())
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

    threads.append(mp.Process(target=oldi))
    threads[-1].start()

    threads.append(mp.Process(target=regard))
    threads[-1].start()

    threads.append(mp.Process(target=dns))
    threads[-1].start()
