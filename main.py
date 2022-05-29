from faker import Faker
import conf
import random
import json

fake = Faker(locale="ru_RU")

def title():
    with open("book.txt","r",encoding='utf-8') as f:
            Book_lines = ""
            Book_line = f.read()
    S = Book_line.split("\n")
    Title = random.choice(S)
    return Title
def year():
    return random.randint(1,2020)
def pages():
    return random.randint(50,2000)
def rating():
    return random.randint(1,5)
def price():
    return random.random()
def author():
    L = []
    for i in range(3):
        name = fake.name()
        L.append(name)
    return L




def dict_generator(pk_d = 1, n = 1):

    pk = pk_d
    for i in range(n):
            Dict = {
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

            yield Dict




if __name__ == '__main__':

    g = dict_generator(n=250)

    L = []
    for i in range(1,250):
          D = next(g)
          L.append(D)

    with open("dict_file.json", "w") as file:
        json.dump(L,file)

    with open("dict_file.json", "r") as file:
        LL = json.load(file)
        print(type(LL))
    for line in LL:
        print(line)








