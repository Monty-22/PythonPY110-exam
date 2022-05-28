import faker
import conf
import random
import sys




def title():
    f = open("book.txt","r",encoding='utf-8')
    Book_lines = ""
    Book_line = f.read()
    S = Book_line.split("\n")
    Title = random.choice(S)
    return Title
def year():
    return random.randint()
def pages():
    return random.randint()
def rating():
    return random.random(1,5)
def price():
    return random.random()
def author():
    L = []
    for i in random.random(1,2,3):
        name = faker.name
        L.append(name)




def dict_generator(pk_d = 1):

    pk = pk_d
    model = conf.model
    Title = ""
    Title = title()
    year = 0
    pages = 0
    rating = 0.0
    year = year()
    pages = pages()
    isbn13 = faker.isbn13
    rating = rating()
    price = 0.0
    price = price()
    author = []
    author = author()
    Dict = {}
    Dict = {
        "model" : model,
        "pk" : pk,
        "fields" : {
            "title" : title,
            "year" : year,
            "pages" : pages,
            "isbn13" : isbn13,
            "rating" : rating,
            "price" : price,
            "author" : author

        }
    }
    pk += 1
    yield Dict




if __name__ == '__main__':
    g = dict_generator()
    L = []
    for i in range(1,100):
      L.append(next(g))




