import time

import undetected_chromedriver as uc

from config import create_folder


@create_folder(dir_name='template')
def main():

    # driver = uc.Chrome()
    # driver.get('https://ya.ru/')

    # with open('index.html', 'w') as file:
    #     file.write(driver.page_source)

    time.sleep(1)


if __name__ == '__main__':
    main()
