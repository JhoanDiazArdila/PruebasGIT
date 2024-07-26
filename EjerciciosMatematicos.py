import os

def clear_screen():
    if os.name == 'nt':  # 'nt' indica Windows
        os.system('cls')
    else:  # Unix/Linux/macOS tienen 'posix'
        os.system('clear')

def suma():
    print("la Suma es ", n1+n2)

def resta():
    resta= n1-n2
    print("La resta es ", resta)

def division ():
    print("La division es ", n1/n2)

def multipli():
    print("La multiplicacion es", n1*n2)

menu_calculadora=("1.Suma","2.Resta","3.Division","4.Multiplicacion", "cualquier otro para salir")

clear_screen()
while True:
    print("*" * 70)
    print("*"*14,"Menu","*"*50)
    print("*" * 70)
    n1=float(input("Ingrese el primer numero de la operacion \n --> "))
    n2=float(input("Ingrese el segundo numero de la operacion \n --> "))
    print("*" * 70)
    for i in menu_calculadora:
        print(i)
    print("*" * 70)
    opc=int(input("Que desea hacer? \n--> "))
    print("*" * 70)
    if opc ==1:
        suma()
    elif opc==2:
        resta()
    elif opc==3:
        division()
    elif opc==4:
        multipli ()
    else:
        print("Adios...")
        break
    print("*" * 70)
    # clear_screen()











