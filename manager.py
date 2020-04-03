import sqlite3 as sql

conn = sql.connect('Main_DataBase_for_Python_Models.db')
cursor = conn.cursor()

sql_viruses = "SELECT * FROM viruses "
cursor.execute(sql_viruses)

viruses = {}
for obj in cursor.fetchall():
    viruses[obj[0]] = [obj[1], obj[2], obj[3]] """ Получаем dict:
                                                 key = virus 
                                                 value = [chance_of_infections, 
                                                            chance_of_mortality_, 
                                                            chance_of_recoveries] """


sql_people = "SELECT * FROM people"
cursor.execute(sql_people)
for person in cursor.fetchall():
    print("{id} | {condition} | {health} | {rationality} | {immune_system} | {chance_of_illnesses} | {chance_of_healthy} | {chance_of_mortality} | {medicine} "\
        .format(id = person[0],
         condition = person[1],
          health = person[2],
           rationality = person[3],
            immune_system = person[4],
             chance_of_illnesses = person[5],
              chance_of_healthy = person[6],
               chance_of_mortality = person[7],
                medicine = person[-1]))

conn.close()
