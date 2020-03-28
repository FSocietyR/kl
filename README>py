
import random
import curses
import colorama
from colorama import Fore




#functions
prov = lambda x,y: x > y
rand = lambda x: int(random.choice(x)) / 100
prinimat = lambda x: x.get(random.choice(list(x.keys())))
sluchainiost = lambda: random.random()
colorama.init()


def zapolnenie_id(C,n,m):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            kniga_id[C] = str(n)+ ';' + str(m)

            C += 1; m += 1
            if m == 30:
                n += 1
                m = 0
            if n == 20:
                n = 0

def zapolenie_knig(X):
    for person in kniga_id:
        X[person] = sluchainiost()

def printMatrix ( matrix ):
   for i in range ( len(matrix) ):
      for j in range ( len(matrix[i]) ):
          print ( "{:2}".format(matrix[i][j]), end = " " )
      print ()

def sozdaniye(matrix):
    for i in range(x):
        matrix.append([])
        for j in range(y):
            matrix[i].append(sost_2)
    matrix[0][0] = sost_1
def main_proverka(x,y):
    while prov(x,y) != True:
        x = rand(l)
    return(x)

prinimat_lecarstva = lambda zdorovie: zdorovie + (prinimat(protivovirusnie) * sluchainiost()) - (zdorovie - smertnost*zdorovie)

def delta_zdorovia(X):
    for key,value in X.items():
        X[key] = prinimat_lecarstva(value)


protivovirusnie = {
        'lecarstvo_1':  -0.1,
        'lecarstvo_2':  0.00,
        'lecarstvo_3':  0.143,
        'lecarstvo_4':  0.179,
        'lecarstvo_5':  0.23,
        'lecarstvo_6': -0.17,
        'lecarstvo_7':  0.07,
        'lecarstvo_8':  0.31,
        'lecarstvo_9':  0.1187,
        'lecarstvo_10': 0.024,
    }




#variables
x = 30
y = 20

sost_1 = '?' #больной
sost_2 = '#' #здоровый
sost_3 = '&' #мертвый
sost_4 = '^' #иммунитет
smertnost = 0.07
matrix = []
shanz_vizdorovlinia = (1 - smertnost) * sluchainiost()
l = [i for i in range (1,101)]

kniga_id = {}
kniga_zdorovia = {}
kniga_uma = {}


n = 0
m = 0
C = 0


immunitet = 1
if __name__ == "__main__":
    shanz_zarazheniya = rand(l)
    shanz_vizdorovlinia = main_proverka(shanz_vizdorovlinia,shanz_zarazheniya)
    main_proverka(shanz_vizdorovlinia,shanz_zarazheniya)
    sozdaniye(matrix)
    zapolnenie_id(C,n,m)
    zapolenie_knig(kniga_uma)
    zapolenie_knig(kniga_zdorovia)
    printMatrix(matrix)
    print(shanz_zarazheniya,shanz_vizdorovlinia,smertnost)
    print(kniga_id,'\n', kniga_zdorovia, '\n', kniga_uma)
    delta_zdorovia(kniga_zdorovia)

    print(kniga_zdorovia)

#TODO: сделать изменение здоровья с течением времени; прописать функцию заражения; прописать функцию смертности;прописать функцию излечения; добавить изменение иммунитета с учетом приема лекарств; добавить коэфициент ума;добавить подключение к sqlite3, весы, и псевдо машинное обучение; добавить анимацию
