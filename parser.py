import requests

web_page = requests.get('https://live.skillbox.ru/playlists/code/python/')

from openpyxl import Workbook
from bs4 import BeautifulSoup
soup = BeautifulSoup(web_page.text, 'html.parser')

soup.find(class_='playlist-inner-card__small-info').text.strip()

'Видео, 01:52:49'.split(',')[-1].strip()

work_book = Workbook()
work_sheet = work_book.active

items = soup.find_all(class_='playlist-inner__item')

for elem in items:
    title = elem.find(class_='playlist-inner-card__link-text').text
    relative_url = elem.find(class_='playlist-inner-card__link').attrs['href']
    timing = elem.find(class_='playlist-inner-card__small-info').text.strip().split(',')[-1].strip()
    url = 'https://live.skillbox.ru' + relative_url
    row = [title, url, timing]
    print(row)
    work_sheet.append(row)

work_book.save('Вебинары про Python от Skillbox.xlsx')