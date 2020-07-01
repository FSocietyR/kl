import sqlite3 as sql
import random

# connection to db

conn = sql.connect('Main_DataBase_for_Python_Models.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS viruses
                        (name text, chance_of_beeig_ill_average float, chance_of_recovery_average float,
                        chance_of_mortality_average float )

""")


def _Write_Into_The_DataBase_Virus(virus, chance_of_infections, chance_of_mortality_, chance_of_recoveries):
    Information_About_Viruses = [str(virus),

                                 chance_of_infections,

                                 chance_of_recoveries,

                                 chance_of_mortality_

                                 ]

    cursor.executemany("INSERT INTO viruses values(?, ?, ?, ?)", Information_About_Viruses)
    conn.commit()


cursor.execute(""" CREATE  TABLE IF NOT EXISTS people
                             (id text, condition text, percent_of_health float, rationality float,
                                   immune_system bool, chance_of_illnesses float,
                                   chance_of_healthy float, chance_of_mortality float,
                                   alive str)
               """)


def _write_into_the_DataBase(person):
    conn = sql.connect('Main_DataBase_for_Python_Models.db')
    cursor = conn.cursor()

    passport = [str(person.id),
                None,
                person.condition,
                person.rationality,
                person.immune_system,
                person.chance_of_illnesses,
                person.chance_of_healthy,
                person.chance_of_mortality,
                str(person.alive),
                0]
    # person.medicine

    cursor.executemany("INSERT INTO people values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (passport,))
    conn.commit()
    del passport
    return('END')


# def request_from_db(id):
#     request_1 = "SELECT condition FROM people where id =?"
#     _request_1 = cursor.execute(request_1, [(str(id))])
#
#     request_2 = "SELECT percent_of_health FROM people where id = ?"
#     _request_2 = cursor.execute(request_2, [(str(id))])
#
#     request_3 = "SELECT chance_of_health FROM people where id = ?"
#     _request_3 = cursor.execute(request_3, [(str(id))])
#
#     if _request_2 > 0.5:
#         if random.random() < _request_3:
#             main_rework = """
#       UPDATE people
#       SET immune_system = int(1)
#       SET condition = 'NOT_ILL_ANYMORE'
#       WHERE id = int(id)"""
#
#             cursor.execute(main_rework)
#             conn.commit()


conn.close()
# TODO: добавить подключение к MatPlotLib и построение графика
# TODO: добавить в *.py изменение лекарств и запись их в БД
