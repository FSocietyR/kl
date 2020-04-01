import sqlite3 as sql
import random

#connection to db
def connection_to_db(cursor):
  conn = sql.connect('Main_DataBase_for_Python_Models)
  cursor = conn.cursor()


cursor.execute(""" CREATE  TABLE people
                                 title(id text, condition text, percent_of_health float, rationality float,  
                                       immune_system bool, y_coordinate int, x_coordinate int,
                                       chance_of_illnesses float, chance_of_healthy float, chance_of_mortality float,
                                       medicine str) 
              """)



def write_into_the_DataBase(person):
  passport = [(str(person), 
          str(person.condition),
          person.percent_of_health,
          person.rationality, 
          person.immune_system, 
          str(person.y_coordinate), 
          str(person.x_coordinate))
          person.chance_of_illnesses,
          person.chance_of_healthy,
          person.chance_of_mortality,
          str(person.medicine)]
  cursor.executemany("INSERT INTO people values(?, ?, ?, ?, ?, ?)", passport)
  conn.commit()

def request_from_db(id):
  
                     
  request_1 = "SELECT condition FROM people where id =?"
  _request_1 = cursor.execute(request_1, [(str(id))])
                     
  request_2 = "SELECT percent_of_health FROM people where id = ?"
  _request_2 = cursor.execute(request_2, [(str(id))]) 
  
  request_3 = "SELECT chance_of_health FROM people where id = ?"
  _request_3 = cursor.execute(request_3, [(str(id))]) 
                     
  if _request_2 > 0.5:
    if random.random() < _request_3:
      main_rework = """
      UPDATE people
      SET immune_system = bool(1)
      SET condition = 'NOT_ILL_ANYMORE'
      WHERE id = int(id)"""
      
      cursosr.execute(main_rework)
      conn.commit()
