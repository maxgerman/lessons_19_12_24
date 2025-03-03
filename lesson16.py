
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

import requests

header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/117.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def get_data_by_selenium(url: str) -> str:
    """Звертається до сервера за url адресою і повертає HTML сайту"""
    service = Service(path="geckodriver")
    driver = webdriver.Firefox(service=service)
    # driver = webdriver.Chrome()
    driver.get(url)
    # пауза для повного завантаження сторінки
    time.sleep(3)
    data = driver.page_source
    driver.quit()
    return data


def parse_data(data: str) -> list:
    """Функція парсингу даних з хтмл документа"""
    res = []

    if data:
        soup = BeautifulSoup(data, "html.parser")
        # li_list = soup.find_all("li", attrs={"class": "catalog-grid__cell"})
        div_list = soup.find_all("div", attrs={"class": "item"})
        # for li in li_list:
        for div in div_list:
            # Пошук тега а
            rz_link = div.find("rz-indexed-link")
            # перша лінка в знайденому по імені елементі
            a = rz_link.find()
            # Беремо у тега а атрибут href
            href = a["href"]

            # Шукаємо тег з інфою
            span = div.find("span", class_="goods-tile__title")

            # За допомогою атрибуту текст, забираємо всю текстову
            # інформацію, що міститься в цьому тегу
            title = span.text.strip()
            old = div.find("div", attrs={"class": "goods-tile__price--old"})
            price = div.find("div", attrs={"class": "goods-tile__price"})
            # Стара ціна є не у всіх, тому потрібно зробити дефолтне значення
            old_price = ""
            if old:
                # Якщо контейнер із старою ціною є
                old = old.text
                # І в цьому контейнер є інфа
                if old:
                    # Забираємо лише те, що є цифрами та формуємо значення ціни
                    old_price = int(
                        "".join(c for c in old if c.isdigit())
                    )  # 14500
            # Звичайна ціна є скрізь, тому формуємо значення
            price = int("".join(c for c in price.text if c.isdigit()))
            # Результат за кожною відеокартою записуємо у вигляді словника
            res.append(
                {
                    "title": title,
                    "href": href,
                    "price": price,
                    "old_price": old_price,
                }
            )
    return res


def save_to_csv(rows) -> None:
    """Функція збереження даних у csv-файл"""
    # comma separated values
    csv_title = ["title", "href", "price", "old_price"]
    with open("videocards.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=csv_title, delimiter=";"
        )  # 2,000.00
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """Головна функція диригент"""
    url = "https://hard.rozetka.com.ua/ua/videocards/c80087/page={}"
    rows = []
    for i in range(20, 21):
        print("getting data...")
        data = get_data_by_selenium(url.format(i))
        time.sleep(3)

        # comparison with requests (no full info)
        data2 = requests.get(url.format(i)).text

        # save for local testing
        print("saving data...")
        with open("data1.html", "w", encoding="utf-8") as f1:
            f1.write(data)


        print("saving data...")
        with open("data2.html", "w", encoding="utf-8") as f:
            f.write(data2)

        # testing with local file
        # with open("data1.html", "r", encoding="utf-8") as f:
        #     data = f.read()

        print("parsing data...")
        rows += parse_data(data)

    print("saving data...")
    save_to_csv(rows)
    print("finished")


if __name__ == "__main__":
    main()




# options / paths:
# web development
# AI/ML
# data science
# devops, testing
# freelance (parsers, bot, automation)


# for all
# git - basic commands, CLI, merge, rebase, conflict resolution, remote (push, pull)
# SQL - databases (select, join, CTE)
# ORM - object relation mapper - SQLAlchemy 2 (async), Django ORM
# asyncio (less multithreading, multiprocessing) - CPU bound tasks, IO bound
# official docs python
# testing - pytest, unittest

# linkedin, djinni, dou

# web
# general: request, response, HTTP, method, status code, DNS (dev.mozilla.org), OSI model

# frameworks: django + DRF (Django Rest Framework), fastapi (tutorial)
# deploy - docker (image, container, build, Dockerfile, docker compose)
# free services: heroku etc
# linux

# algorithms and datastructures - live coding (leetcode, hackerrank, codewars)
# SOLID, patterns