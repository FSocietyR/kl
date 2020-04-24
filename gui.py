import tkinter as tk
import sqlite3 as sqlite3
import tkinter.ttk as ttk


# $functions
def fill_in_the_tables():
    import manager.py

    dictionary_with_conditions = {'cond_1': 0,

                                  'cond_2': 0,

                                  'cond_3': 0,

                                  'cond_4': 0,

                                  'cond_5': 0}


    NULL_MASSSIVE = manager._getting_information_from_db()  """return massive m[0] = 'CONDTIDIONS'
                                                                m[1] = cond_1
                                                                m[2] = cond_2
                                                                m[3] = cond_3
                                                                m[4] = cond_4
                                                                m[5] = cond_5"""
    for i in range(1,6):
        dictionary_with_conditions['cond_' + str(i)] = NULL_MASSSIVE[i]

    del NULL_MASSSIVE

root = tk.Tk()
root.geometry('300x400')



root.mainloop()
