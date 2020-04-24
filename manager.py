import sqlite3 as sql


def _writing_viruses():

    conn = sql.connect('Main_DataBase_for_Python_Models.db')
    cursor = conn.cursor()

    sql_viruses = "SELECT * FROM viruses "
    cursor.execute(sql_viruses)

    viruses = {}
    for obj in cursor.fetchall():
        viruses[obj[0]] = [obj[1], obj[2], obj[3]]
    conn.close()

    return(0)

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
    if finish_function() == 0:

        conn = sql.connect('Main_DataBase_for_Python_Models.db')
        cursor = conn.cursor()

        command = "SELECT * FROM people"
        cursor.execute(command)

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
            day = person[-1]
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
                    else:
                        if r < person[5]:
                            rework = """
                            UPDATE people
                            SET condition = 'ILL',
                            immune_system = ?,
                            percent_of_health = ?
                            WHERE identifier = ?"""
                            data = (0, accepting, person[0])
                            cursor.execute(rework, (data[0], data[1], data[2]))
                            conn.commit()
                        else:
                            rework = """
                            UPDATE people
                            SET percent_of_health = ?
                            WHERE identifier = ?"""
                            data = (accepting, person[0])
                            cursor.execute(rework, (data[0], data[1]))
                            conn.commit()

                print(person)
            if person[1] != 'DEAD':
                rework = """
                UPDATE people
                SET DAY = ?
                WHERE identifier = ?"""
                day += 1
                cursor.execute(rework, (day, person[0]))
                conn.commit()
        conn.close()
        import time
        time.sleep(5)
        return(0)

    else:
        exit(0)
def accept_medicine_(health, mortal):
    import main_model

    return (health * 1.37 + 2 * (
            main_model.accept_(medicine.medicine_anti_virus) * main_model.randomise_()) - (
                    health * (1 - mortal)))


def Print_Database():
    conn = sql.connect('Main_DataBase_for_Python_Models.db')
    cursor = conn.cursor()

    command = "SELECT * FROM people"
    cursor.execute(command)

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

def _getting_information_from_db(request):

    conn = sql.connect('Main_DataBase_for_Python_Models.db')
    cursor = conn.cursor()

    command = "SELECT * FROM people"
    cursor.execute(command)
    if request == 'condition':
        NULL_MASSSIVE = {'name' : 'CONDITIONS',
                         'cond_1' : 0,
                          'cond_2' : 0,
                           'cond_3' : 0,
                            'cond_4' : 0,
                             'cond_5' : 0}

        for person in cursor.fetchall():

            if person[1] == None:
                NULL_MASSSIVE['cond_2'] = NULL_MASSSIVE['cond_2'] + 1

            if person[1] == 'ILL':
                NULL_MASSSIVE['cond_1'] = NULL_MASSSIVE['cond_1'] + 1

            if person[1] == 'DEAD':
                NULL_MASSSIVE['cond_3'] = NULL_MASSSIVE['cond_3'] + 1

            if person[1] == 'NOT_ILL_ANYMORE':
                NULL_MASSSIVE['cond_4'] = NULL_MASSSIVE['cond_4'] + 1
        conn.close()
        return(NULL_MASSSIVE)
        del NULL_MASSSIVE

    elif request == 'graph':
        NULL_DICTIONARY = {'name': 'HEALTH'}

        for person in cursor.fetchall():
            NULL_DICTIONARY[str(person[0])] = person[3]

        conn.close()
        return(NULL_DICTIONARY)
        del NULL_DICTIONARY

        conn.close()
# TODO: REWORK THIS FUNCTION

def finish_function():

    conn = sql.connect('Main_DataBase_for_Python_Models.db')
    cursor = conn.cursor()

    command = "SELECT * FROM people"
    cursor.execute(command)
    lst = []
    for person in cursor.fetchall():
        if person[1] != 'DEAD':
            lst.append(person[1])
    if all(condition == 'NOT_ILL_ANYMORE' for condition in lst):
        return(1)
    else:
        return(0)

    conn.close()


if __name__ == "__main__":
    for i in range(20):
        _checking_condition()
# TODO: добавить к ill: если кол-во дней < random.randrange(massive) massive = [i for i in range (0,10)], То поставить person[1] = 'incubation'
