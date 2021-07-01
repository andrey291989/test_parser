from bs4 import BeautifulSoup
from urllib.request import *
import yaml
import os

with open('info.yaml') as file:
    templates = yaml.safe_load(file)

url = templates['url']
count = templates['quantity']
folder_name = templates['folder']


def new_folder(folder: str) -> None:
    """
    Проверяет создана ли папка если нет то создает ее
    :param folder: имя папки
    :type folder: str
    """
    if not os.path.isdir(folder):
        os.mkdir(folder)


def get_html(url: str) -> str:
    """
    Скачивает содержимое странички
    :param url: url странички
    :return: html веб страницы
    """
    req = Request(url)
    html = urlopen(req).read()
    return html



def main(num: int, folder_name: str) -> None:
    """
    Скачиваем определенное кол-во изображений
    в указанную папку
    :param num: количество изображений
    :param folder_name: имя папки
    """
    new_folder(folder_name)
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.find_all(class_='serp-item__thumb justifier__thumb')
    for num_img in range(num):
        image = lis[num_img]['src']
        urlretrieve('https:' + image, folder_name + '/' + str(num_img) + '.jpg')
        print(str(num_img) + '.jpg Скачен')

        if __name__ == '__main__':
            main(count, folder_name)
