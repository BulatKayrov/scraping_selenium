import time

import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from decorators_tools import create_folder, hidden_chrome

URL = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/'
DATA = []


@hidden_chrome
def driver_connect(url: str):
    driver = uc.Chrome()
    driver.get(url)
    time.sleep(3)

    return driver.page_source


@create_folder(dir_name='template')
def get_page_count(url: str):
    """Получение количества страниц"""

    html_ = driver_connect(url=url)

    soup = BeautifulSoup(html_, 'lxml')
    pages = (
        soup.find('ul', class_='pagination-widget__pages')
        .find_all('li', class_='pagination-widget__page')
    )

    total_pages = (
        pages[-1].find('a', class_='pagination-widget__page-link pagination-widget__page-link_last').
        get('href').split('?p=')[-1]
    )

    with open('template/page_1.html', 'w') as file:
        file.write(html_)

    return int(total_pages)


def save_pages_all(url: str, page: int):
    link = f'{url}?p={page}'
    html_ = driver_connect(url=link)

    with open(f'template/page_{page}.html', 'w') as file:
        file.write(html_)


def main():
    count = get_page_count(url=URL)

    for page in range(2, count + 1):
        save_pages_all(url=URL, page=page)

        print(f'Страница {page} сохранена')


if __name__ == '__main__':
    main()
