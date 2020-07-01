
from tkinter import *

from PIL import Image as img
from PIL import ImageTk as imgtk

import numpy.random as rand_
import time

# $functions


class Objcts:


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
        canvas = Canvas(root, width = 1000, height = 1000 )
        canvas.pack()

        def motion(counter):
            for i in range(20):
                for j in range(counter):
                    tag = 'person_{}'.format(counter)
                    canvas.move(tag, movement()[0], movement()[1])
                    canvas.update()
                    time.sleep(2)

        def movement() -> list:

            import random
            import math
            alpha = math.radians(int(random.random()) * 100)
            # X_standart = 0
            # Y_standart = 0
            Z_standart = 10
            Z_for_person = Z_standart*random.random() + random.random()
            matrix = [Z_for_person*math.sin(alpha)+random.random(), Z_for_person*math.cos(alpha) - random.random()]
            return matrix  # returns a triangle with
            # leg Y and leg X

            # while canvas.coords(obj)[1] < 700:
            #     time.sleep(5)
            #     motion(obj, Request)#Please notice! (from manual) You can also omit the callback. If you do,
            #                                 this method simply waits for the given number of milliseconds,
            #                                 without serving any events (same as time.sleep(delay_ms*0.001)).
            #     canvas.update()#!!
        c = 0
        for i in range(1, 6):
            dwc = Objcts.fitt()
            print(dwc)
            g = globals()
            list_name = 'l_{}'.format(i)
            g[list_name] = []
            for obct in range(dwc['cond_' + str(i)][0][0]):

                coordinates = rand_.sample(2) #координаты на canvas
                X = coordinates[0]*1000
                Y = coordinates[1]*1000
                path = img.open('ball_{}.png'.format(i))
                image_name = 'i_{}'.format(obct)
                objct = 'o_{}'.format(obct)
                g[image_name] = imgtk.PhotoImage(path)
                g[list_name].append(g[image_name])
                if i != 3:
                    g[objct] = canvas.create_image(X, Y, image=g[image_name], tag='person_{}'.format(c))
                    c+=1
                else:
                    g[objct] = canvas.create_image(X, Y, image=g[image_name], tag='dead')
        motion(c)



        root.mainloop()

if __name__ == "__main__":
    Objcts.main()
