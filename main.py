import requests
from bs4 import BeautifulSoup
import json

url = "https://api.technodom.kz/katalog/api/v1/products/category/smartfony?city_id=5f5f1e3b4c8a49e692fefd70&limit=20&brands=apple&sorting=score&price=0"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
data = json.loads(soup.text)

apple_256_names = []
for product in data.get('payload')[:20]:
    for description in product.get('short_description'):
        if description.get('values')[0].get('value_ru') == '256':
            apple_256_names.append(product.get('title'))

with open('apple.json', 'w', encoding='utf-8') as file:
    json.dump(apple_256_names, file, indent=2, ensure_ascii=False)
    print("created")
