from bs4 import BeautifulSoup
import requests

# URL
url = 'http://mignews.com/mobile'
page = requests.get(url)

# check connection:
print(page.status_code)

# Processs HTML with bs4
soup = BeautifulSoup(page.text, "html.parser")

# filtered_news list
filtered_news = []

# find all news posts
all_news = soup.findAll('article', class_='post mb-2')

# filter on right button
for article in all_news:
    if article.find('div', 'btn btn-primary btn-xs rounded-0') is not None:
        filtered_news.append(article)

# extract titles from filtered_news
titles = []
for article in filtered_news:
    title_tag = article.find('div', class_='text-color-dark').find('a')  # Найдите ссылку с текстом заголовка
    if title_tag:
        titles.append(title_tag.get_text(strip=True))  # Извлекаем текст заголовка

# print results
for title in titles:
    print(title)
