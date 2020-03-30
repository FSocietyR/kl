import random

import colorama
from colorama import Fore

# functions
prov_ = lambda x, y: x > y

accept_ = lambda x: x.get(random.choice(list(x.keys())))  # принимать лекарства

randomise_ = lambda: random.random()  # возвращает рандомное число

rand_ = lambda x: (int(random.choice(x)) / 100) * randomise_()  # возвращает рандомный кэф из последовательности

random_id = lambda x: random.randrange(0,599)


def creation_of_mortality():
    mortality = randomise_()
    while mortality > 0.1732241 or mortality < 0.073:
        mortality = randomise_()
    return (mortality)


class clear_the_screen:
    def __repr__(self):
        import os
        import time
        time.sleep(3)
        os.system('cls')
        return

class books():

    book_of_id = {}  # словарь с id и координатами
    book_of_health = {}  # хранятся key = id value = health
    book_of_rationalities = {}  # хранятся key = id, value = rationality
    book_of_immune_system = {} # хранятся key = id, value = immune
    book_of_aliveness = {}

    def zapolnenie_id(C, n, m):

        for i in range(len(matrix)):

            for j in range(len(matrix[i])):

                books.book_of_id[C] = str(n) + ';' + str(m)

                C += 1
                m += 1
                if m == 10:
                    n += 1
                    m = 0
                if n == 10:
                    n = 0


    def zapolenie_knig(X):
        for person in books.book_of_id:
            X[person] = randomise_()

    def creation_book_of_aliveness():

        for person in books.book_of_id:

            if books.book_of_health[person] > 0:
                books.book_of_aliveness[person] = 1

            else:
                books.book_of_aliveness[person] = 'DEAD'
                books.book_of_health[person] = 'NOT ALIVE, SORRY'

def print_Matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:2}".format(matrix[i][j]), end=" ")
        print()


def sozdaniye_matrix(matrix):
    for i in range(x):
        matrix.append([])
        for j in range(y):
            matrix[i].append(conditions_of_people.cond_2)
    matrix[0][0] = conditions_of_people.cond_1


def main_proverka(x, y):
    while prov_(x, y) != True:
        x = (1 - mortality) * randomise_()
        if x > chance_of_infections - mortality:
            x -= mortality
    return (x)


accept_medicine = lambda health: health * 1.37 + 2 * (accept_(medicine_anti_virus.anti_virus) * randomise_()) - (
        health * (1 - mortality))


def delta_zdorovia(X):
    for key, value in X.items():
        try:
            X[key] = accept_medicine(value)
        except TypeError:
            pass

def counter():
    import time
    from time import sleep
    counter = 0
    for i in range(120):
        delta_zdorovia(books.book_of_health)
        People.create_main_dictionary_for_class_people()
        cls = clear_the_screen()
        cls.__repr__()
        print('DAY {}'.format(counter))

        print_Matrix(matrix)
        print(chance_of_infections, chance_of_recoveries, mortality)
        counter+=1

class medicine_anti_virus:
    anti_virus = {
        'medicine_1': -0.1,
        'medicine_2': 0.00,
        'medicine_3': 0.143,
        'medicine_4': 0.179,
        'medicine_5': 0.23,
        'medicine_6': -0.17,
        'medicine_7': 0.07,
        'medicine_8': 0.31,
        'medicine_9': 0.1187,
        'medicine_10': 0.024,
    }

# variables
x = 10  # количество людей по оси OY
y = 10  # количество людей по оси OX
n = 0  # y-координата
m = 0  # x-координата
C = 0  # id


class conditions_of_people:
    cond_1 = '*'  # больной
    cond_2 = '#'  # здоровый
    cond_3 = '&'  # мертвый
    cond_4 = '^'  # иммунитет
    cond_5 = '?'  # период инкубации


mortality = creation_of_mortality() #до тех пор пока mortality > 0.17.... он будет создавать новое значение
matrix = []
chance_of_recoveries = (1 - mortality) * randomise_()
massive_with_numbers = [i for i in range(1, 101)]

# Подключение словарей


class People:


    def __init__(self, id, condition, rationality, alive, y_coordinate, x_coordinate):
        self.id = id
        self.condition = condition
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.rationality = rationality
        self.alive = alive
        # self.immune_sistem = immune_sistem


    def checking_the_infection(alive, condition_of_person):
        try:
            if alive != 'DEAD' or alive != 0:
                return(condition_of_person>chance_of_infections)
            else:
                return ('DEAD')
        except TypeError:
            pass

    def function_of_infection_person(person, condition_of_person, alive, y_coordinate_of_person, x_coordinate_of_person):

        if People.checking_the_infection(alive, condition_of_person) == 'DEAD':
            matrix[y_coordinate_of_person][x_coordinate_of_person] = conditions_of_people.cond_3
            person.alive = 0
        else:
            if People.checking_the_infection(alive,condition_of_person) == True:
                matrix[y_coordinate_of_person][x_coordinate_of_person] = conditions_of_people.cond_2
            else:
                matrix[y_coordinate_of_person][x_coordinate_of_person] = conditions_of_people.cond_1


    def immune_sistem():
        pass
    def create_main_dictionary_for_class_people():
        for person in books.book_of_id:

            person = People(person,books.book_of_health[person],books.book_of_rationalities[person], books.book_of_aliveness[person], int(books.book_of_id[person][0]), int(books.book_of_id[person][-1]))
            People.function_of_infection_person(person, person.condition, person.alive, person.y_coordinate, person.x_coordinate)

immunitet = 1







if __name__ == "__main__":
    chance_of_infections = rand_(massive_with_numbers)
    chance_of_recoveries = main_proverka(chance_of_recoveries, chance_of_infections)
    main_proverka(chance_of_recoveries, chance_of_infections)
    sozdaniye_matrix(matrix)
    books.zapolnenie_id(C, n, m)
    books.zapolenie_knig(books.book_of_rationalities)
    books.zapolenie_knig(books.book_of_health)
    books.creation_book_of_aliveness()
    print_Matrix(matrix)
    print(chance_of_infections, chance_of_recoveries, mortality)
    cls = clear_the_screen()
    # print(book_of_id, '\n', book_of_health, '\n', book_of_rationalities)

    # print(book_of_health)
    counter()


# TODO: прописать функцию заражения; прописать функцию смертности;прописать функцию излечения; добавить изменение иммунитета с учетом приема лекарств; добавить коэфициент ума;добавить подключение к sqlite3, весы, и псевдо машинное обучение; добавить анимацию
# TODO: написать функцию появления имунной сиситемы: после того как человек вылечился  random.randrange(0,1) если 1: иммунитет, так же добавить в объект класса был ли он болен (1,2) 1: был, 2 : не был
# TODO: добавить from tkinter import *; объекты: на каждый cond; анимацию с ними (перестроить весь код на tkinter)
# TODO: сделать так чтобы если человек умер, то он был мертв и заболеть уже не мог
