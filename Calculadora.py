from main import *

def menu():
    calc1 = Calc()
    while (True):
        calc1.menu()
        op = int(input('Introduce tu opcion:'))
        if (op == 0):
            break
        else:
            x = int(input('ingresa el primer numero: '))
            y = int(input('ingresa el segundo numero: '))
            if (op == 1):
                print(calc1.sumar(x,y))
            elif (op == 2):
                print(calc1.resta(x, y))
            elif (op == 3):
                print(calc1.multi(x, y))
            elif (op == 4):
                print(calc1.div(x,y))
                
if __name__ ==  '__main__':
    menu()



