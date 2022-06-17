import conf
import random
import json
from typing import Union,List
from faker import Faker

fake = Faker(locale="ru_RU")

def title() ->str:
    """Функция возвращает случайным образом выбранное название книги """
    with open("book.txt","r",encoding='utf-8') as f:
            book_lines: str = ""
            book_line = f.read()
    s: List[str] = book_line.split("\n")
    title_: str = random.choice(s)
    return title_


def year() -> int:
    return random.randint(1,2020)


def pages() -> int:
    return random.randint(50,2000)


def rating() -> int:
    return random.randint(1,5)


def price() -> Union[int, float]:
    return random.random()


def author() -> list:
    list_1: list = []
    for _ in range(3):
        name = fake.name()
        list_.append(name)
    return list_1


def dict_generator(pk_d: int = 1, n: int = 1):
    """Возвращает генератор словарей с атрибутами книг"""
    pk = pk_d
    for _ in range(n):
            dict_1: dict = {
                "model" : conf.model,
                "pk" : pk,
                "fields" : {
                    "title" : title(),
                    "year" : year(),
                    "pages" : pages(),
                    "isbn13" : fake.isbn13(),
                    "rating" : rating(),
                    "price" : price(),
                    "author" : author()

                }
            }
            pk += 1
            yield dict_1


if __name__ == '__main__':

    g = dict_generator(n = 250)

    list_ = []
    for _ in range(1,250):
          dict_ = next(g)
          list_.append(dict_)

    with open("dict_file.json", "w") as file:
        json.dump(list_,file)

    with open("dict_file.json", "r") as file:
        LL = json.load(file)









