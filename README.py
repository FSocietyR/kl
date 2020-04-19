import random

import database_connection as db

prov_ = lambda x, y: x > y

accept_ = lambda x: x.get(random.choice(list(x.keys())))  # принимать лекарства

randomise_ = lambda: random.random()  # возвращает рандомное число

rand_ = lambda x: (int(random.choice(x)) / 100) * randomise_()  # возвращает рандомный кэф из последовательности

random_id = lambda x: random.randrange(0, 599)


def creation_of_mortality():
    mortality = randomise_()
    while mortality > 0.1732241 or mortality < 0.073:
        mortality = randomise_()
    return (mortality)


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


class books():
    book_of_id: dict = {}  # словарь с id и координатами
    book_of_health: dict = {}  # хранятся key = id value = health
    book_of_rationalities: dict = {}  # хранятся key = id, value = rationality
    book_of_immune_system: dict = {}  # хранятся key = id, value = immune
    book_of_recoveries: dict = {}  # key = id | value = chance_of_recoveries
    book_of_infections: dict = {}
    book_of_mortality: dict = {}
    book_of_working_medicine_percentage: dict = {}

    def filling_the_id(id_position: int, oy_coordinate, ox_coordinate):

        for i in range(len(matrix)):

            for j in range(len(matrix[i])):

                books.book_of_id[id_position] = str(oy_coordinate) + ';' + str(ox_coordinate)

                id_position += 1
                ox_coordinate += 1
                if ox_coordinate == 10:
                    oy_coordinate += 1
                    ox_coordinate = 0
                if oy_coordinate == 10:
                    oy_coordinate = 0

    def creeation_of_books(book: dict):
        for person in books.book_of_id:
            book[person] = randomise_()

    def creation_of_book_of_chances(self: dict, chance_of_whatever: str) -> None:
        counter = 0
        sum = 0

        def what_is_whatever(chance_of_whatever: str) -> float:

            if chance_of_whatever == 'infection':
                chance_of_whatever: float = 0
                while (chance_of_whatever / chance_of_infections) < 0.9378765845:
                    chance_of_whatever = randomise_()
                return (chance_of_whatever)

            if chance_of_whatever == 'mortality':
                chance_of_whatever: float = 1.00
                while (chance_of_whatever / chance_of_mortality_) > 0.75:
                    chance_of_whatever = randomise_()
                return (chance_of_whatever)

            if chance_of_whatever == 'recovery':
                chance_of_whatever: float = 0
                while (chance_of_whatever / chance_of_recoveries) < chance_of_infections:
                    chance_of_whatever = randomise_()
                return (chance_of_whatever)

            if chance_of_whatever == 'medicine':

                def chance_of_working_medicine() -> list:
                    massive = []
                    for medicine in medicine_anti_virus.anti_virus:
                        chance_of_whatever = randomise_()

                        massive.append(chance_of_whatever)
                    return massive

                for person in books.book_of_id:
                    books.book_of_working_medicine_percentage[person] = chance_of_working_medicine()

        for person in books.book_of_id:

            if chance_of_whatever != 'medicine':
                self[person] = what_is_whatever(chance_of_whatever)
                sum += what_is_whatever(chance_of_whatever)
                counter += 1

            else:
                what_is_whatever(chance_of_whatever)
                break

        # returns average keys in dict
        try:
            return print(sum / counter)

        except ZeroDivisionError:
            pass


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


class People:

    def __init__(self, id: int, condition: str, immune_system: bool, rationality: float, alive: bool,
                 chance_of_infection: float, chance_of_recovery: float, chance_of_mortality: float, y_coordinate: int,
                 x_coordinate: int) -> None:
        self.id = id
        self.condition = condition
        self.immune_system = immune_system
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.rationality = rationality
        self.chance_of_illnesses = chance_of_infection
        self.chance_of_healthy = chance_of_recovery
        self.chance_of_mortality = chance_of_mortality
        self.alive = alive

    # def checking_the_infection(alive, condition_of_person):
    #     try:
    #         if alive != 'DEAD' or alive != 0:
    #             return condition_of_person > chance_of_infections
    #         else:
    #             return 'DEAD'
    #     except TypeError:
    #         pass
    #
    # def function_of_infection_person(person, condition_of_person, alive, y_coordinate_of_person,
    #                                  x_coordinate_of_person):
    #
    #     if People.checking_the_infection(alive, condition_of_person) == 'DEAD':
    #
    #         matrix[y_coordinate_of_person][x_coordinate_of_person] = conditions_of_people.cond_3
    #         person.alive = 0
    #
    #     else:
    #
    #         if People.checking_the_infection(alive, condition_of_person) == 1:
    #
    #             matrix[y_coordinate_of_person][x_coordinate_of_person] = conditions_of_people.cond_2
    #
    #         else:
    #
    #             matrix[y_coordinate_of_person][x_coordinate_of_person] = conditions_of_people.cond_1[

    def create_main_dictionary_for_class_people():
        for person in books.book_of_id:

            person = People(person,
                            books.book_of_health[person],
                            0, books.book_of_rationalities[person],
                            1, books.book_of_infections[person],
                            books.book_of_recoveries[person],
                            books.book_of_mortality[person],
                            int(books.book_of_id[person][0]),
                            int(books.book_of_id[person][-1])
                            )
            db._write_into_the_DataBase(person)
            # db.request_from_db(person)

            # People.function_of_infection_person(person, person.condition, person.alive, person.y_coordinate,
            #                                     person.x_coordinate)


# constants
x = 10  # количество людей по оси OY
y = 10  # количество людей по оси OX
oy_coordinate = 0  # y-координата
ox_coordinate = 0  # x-координата
id_position = 0  # id


class conditions_of_people:
    cond_1 = '*'  # больной
    cond_2 = '#'  # здоровый
    cond_3 = '&'  # мертвый
    cond_4 = '^'  # иммунитет
    cond_5 = '?'  # период инкубации


mortality = creation_of_mortality()  # до тех пор пока mortality > 0.17.... он будет создавать новое значение
matrix = []
chance_of_recoveries = (1 - mortality) * randomise_()
massive_with_numbers = [i for i in range(1, 101)]

if __name__ == "__main__":
    chance_of_mortality_ = creation_of_mortality()

    chance_of_infections = rand_(massive_with_numbers)

    chance_of_recoveries = main_proverka(chance_of_recoveries, chance_of_infections)

    main_proverka(chance_of_recoveries, chance_of_infections)

    sozdaniye_matrix(matrix)

    books.filling_the_id(id_position, oy_coordinate, ox_coordinate)

    books.creeation_of_books(books.book_of_rationalities)

    books.creeation_of_books(books.book_of_health)

    books.creation_of_book_of_chances(books.book_of_infections, 'infection')

    books.creation_of_book_of_chances(books.book_of_mortality, 'mortality')

    books.creation_of_book_of_chances(books.book_of_recoveries, 'recovery')

    books.creation_of_book_of_chances(books.book_of_working_medicine_percentage, 'medicine')

    People.create_main_dictionary_for_class_people()

    # print(books.book_of_infections)
    #
    # print(books.book_of_mortality)
    #
    # print(books.book_of_recoveries)
    #
    # print(books.book_of_working_medicine_percentage)
    #
    # print(books.book_of_id)
