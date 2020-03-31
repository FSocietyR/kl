import tkinter
from tkinter import *

root = Tk()
root.geometry ('400x300')

class Widjets:
    counter_for_condtition_1 = 0
    counter_for_condtition_2 = 0
    counter_for_condtition_3 = 0
    counter_for_condtition_4 = 0
    counter_for_condtition_5 = 0
    
    def __init__(self, condition):    
        
        if condition == 'ILL'
            counter_for_condtition_1+=1
            
        if condition == 'ALIVE'
            counter_for_condtition_2+=1 
        
        if condition == 'DEAD:
            counter_for_condtition_3+=1 
    def create_circles():
        for i in range(counter_for_condition_1):
            pass
 
# TODO: сделать привязку к БД на sqlite3 со столбцом id; condition; alive; immune_system; потом выгружать эти данные на gui.py И отображать с помощью tkinter или pygame
