import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

listings = []

for page in range(1, 501):  
    url = f"https://krisha.kz/prodazha/kvartiry/almaty/?page={page}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    cards = soup.find_all('div', class_='a-card')
    
    for card in cards:
        try:
            # Название (комнаты и площадь)
            title = card.find('a', class_='a-card__title')
            title = title.text.strip() if title else None

            # Цена
            price = card.find('div', class_='a-card__price')
            price = price.text.strip() if price else None

            # Адрес
            address = card.find('div', class_='a-card__subtitle')
            address = address.text.strip() if address else None

            # Описание (тип дома, год, этаж)
            desc = card.find('div', class_='a-card__text-preview')
            desc = desc.text.strip() if desc else None

            if title and price:
                listings.append({
                    'title': title,
                    'price': price,
                    'address': address,
                    'description': desc
                })
        except:
            continue
    
    print(f"Страница {page} — {len(listings)} объявлений")
    time.sleep(1)

df = pd.DataFrame(listings)
df.to_csv('krisha_raw.csv', index=False, encoding='utf-8-sig')
print(f"\nГотово! Всего: {len(df)} объявлений")
print(df.head())