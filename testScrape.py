import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/gp/product/B00TLEMRKM?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=2VKMNKK1KK20M5KP0YHD'
headers = {
  "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3955.0 Safari/537.36 Edg/80.0.327.0'}

def check_price():
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'lxml')
  title = soup.find(id='productTitle')
  price = soup.find(id='priceblock_dealprice').get_text()
  convertedPrice = float(price[1:5])

  print(convertedPrice)
  print(title)
  print('$' + str(convertedPrice))
