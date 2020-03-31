import sqlite3 as sql

#connection to db
conn = sql.connect('Main_DataBase_for_Python_Models)
cursor = conn.cursor()


cursor.execute(""" CREATE  TABLE people
                                 title(id text, condition text, rationality float,  
                                       immune_system bool, y_coordinate int, x_coordinate int) 
              """)



def write_into_the_DataBase(person):
  passport = [(str(person), 
          str(person.condition), 
          person.rationality, 
          person.immune_system, 
          str(person.y_coordinate), 
          str(person.x_coordinate))]
cursor.executemany("INSERT INTO people values(?, ?, ?, ?, ?, ?)", passport)
conn.commit()
