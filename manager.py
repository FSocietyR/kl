import sqlite3 as sql

conn = sql.connect('Main_DataBase_for_Python_Models.db')
cursor = conn.cursor()

sql_viruses = "SELECT * FROM viruses "
cursor.execute(sql_viruses)

viruses = {}
for obj in cursor.fetchall():
    viruses[obj[0]] = [obj[1], obj[2], obj[3]]

sql_people = "SELECT * FROM people"
cursor.execute(sql_people)


class medicine:
    medicine_anti_virus = {
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


def _checking_condition():

    conn = sql.connect('Main_DataBase_for_Python_Models.db')
    cursor = conn.cursor()

    sql_people = "SELECT * FROM people"
    cursor.execute(sql_people)

    import main_model

    medicine_anti_virus = {
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

    dictionary_with_conditions = {'cond_1': 0,

                                  'cond_2': 0,

                                  'cond_3': 0,

                                  'cond_4': 0,

                                  'cond_5': 0}

    for person in cursor.fetchall():

        health = person[2]
        mort = person[7]
        accepting = accept_medicine_(health, mort)
        main_id = person[5]
        r = main_model.randomise_()

        if health < 0.15:

            if health > 0.03:



                if r > mort:  # check if person can beat the illnesses

                    if r < main_id:
                        rework = """
                            UPDATE people
                            SET condition = 'NOT_ILL_ANYMORE',
                            immune_system = ?,
                            percent_of_health = ?
                            WHERE identifier = ?"""

                        data = (1, accepting, (person[0]))
                        cursor.execute(rework, (data[0], data[1], data[2]))
                        conn.commit()
                    else:

                        rework = """
                            UPDATE people
                            SET condition = 'ILL',
                            percent_of_health = ?
                            WHERE identifier = ? """
                        data = (accepting, (person[0]))
                        cursor.execute(rework, (data[0], data[1]))
                        conn.commit()

                else:

                    rework = """
                        UPDATE people
                        SET condition = 'ILL',
                        percent_of_health = ?
                        WHERE identifier = ? """
                    data = (accepting, (person[0]))
                    cursor.execute(rework, (data[0], data[1]))
                    conn.commit()

            else:

                rework = """
                    UPDATE people
                    SET condition = ?,
                    percent_of_health = ?
                    WHERE identifier = ?"""
                data = ('DEAD', 0.00, (person[0]))
                cursor.execute(rework, (data[0], data[1], data[2]))
                conn.commit()

        else:

            if person[1] == 'ILL':

                if r < person[5]:
                    rework = """
                    UPDATE people
                    SET condition = 'NOT_ILL_ANYMORE',
                    immune_system = ?,
                    percent_of_health = ?
                    WHERE identifier = ?"""
                    data = (1, accepting, (person[0]))
                    cursor.execute(rework, (data[0], data[1], data[2]))
                    conn.commit()
                else:

                    rework = """
                    UPDATE people
                    SET condition = 'ILL',
                    percent_of_health = ?
                    WHERE identifier = ? """
                    data = (accepting, person[0])
                    cursor.execute(rework, (data[0], data[1]))
                    conn.commit()

            else:
                if person[4] == 1:
                    rework = """
                    UPDATE people
                    SET condition = 'NOT_ILL_ANYMORE',
                    immune_system = ?,
                    percent_of_health = ?
                    WHERE identifier = ?"""
                    data = (1, accepting, person[0])

                    cursor.execute(rework, (data[0], data[1], data[2]))
                    conn.commit()
            print(person)
    conn.close()
def accept_medicine_(health, mortal):
    import main_model

    return (health * 1.37 + 2 * (
            main_model.accept_(medicine.medicine_anti_virus) * main_model.randomise_()) - (
                    health * (1 - mortal)))


def Print_Database():
    conn = sql.connect('Main_DataBase_for_Python_Models.db')
    cursor = conn.cursor()

    for person in cursor.fetchall():
        print(
            "{id} | {condition} | {health} | {rationality} | {immune_system} | {chance_of_illnesses} | {chance_of_healthy} | {chance_of_mortality} | {medicine} " \
                .format(id=person[0],
                        condition=person[1],
                        health=person[2],
                        rationality=person[3],
                        immune_system=person[4],
                        chance_of_illnesses=person[5],
                        chance_of_healthy=person[6],
                        chance_of_mortality=person[7],
                        medicine=person[-1]))


conn.close()

if __name__ == "__main__":

    _checking_condition()


