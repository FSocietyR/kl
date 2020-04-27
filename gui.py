import tkinter
from tkinter import *
from PIL import *
from PIL import Image as img
from PIL import ImageTk as imgtk
import sqlite3 as sqlite3 #preinstall
import tkinter.ttk as ttk # will be ready after installing tkinter
import numpy.random as rand_

# $functions


class Objcts():


    def fitt(): #fill_in_the_tables
        import manager

        dictionary_with_conditions = {'cond_1': 0,

                                      'cond_2': 0,

                                      'cond_3': 0,

                                      'cond_4': 0,

                                      'cond_5': 0}


        NULL_MASSIVE = manager._getting_information_from_db('condition')
        for i in range(1,6):
            dictionary_with_conditions['cond_' + str(i)] = NULL_MASSIVE['cond_' + str(i)]

        del NULL_MASSIVE
        return dictionary_with_conditions

def  main():
    import main_model
    root = Tk()
    root.geometry('1001x1001')
    canvas = Canvas(root, width =1000, height = 1000 )
    canvas.grid()
    for i in range(1,6):

        dwc = Objcts.fitt()
        g = globals()
        list_name = 'l_{}'.format(i)
        g[list_name] = []
        for obct in range(dwc['cond_' + str(i)]):

            coordinates = rand_.sample(2) #координаты на canvas
            X = coordinates[0]*1000
            Y = coordinates[1]*1000
            path = img.open('ball_{}.png'.format(i))
            image_name = 'i_{}'.format(obct)
            g[image_name] = imgtk.PhotoImage(path)
            g[list_name].append(g[image_name])
            canvas.create_image(X, Y, image = g[image_name] )

    root.mainloop()

if __name__ == "__main__":
    main()
