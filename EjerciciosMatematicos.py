import os
import json
import pathlib



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


# while True:
#     print("*" * 70)
#     print("*"*14,"Menu","*"*50)
#     print("*" * 70)
#     n1=float(input("Ingrese el primer numero de la operacion \n --> "))
#     n2=float(input("Ingrese el segundo numero de la operacion \n --> "))
#     print("*" * 70)
#     for i in menu_calculadora:
#         print(i)
#     print("*" * 70)
#     opc=int(input("Que desea hacer? \n--> "))
#     print("*" * 70)
#     if opc ==1:
#         suma()
#     elif opc==2:
#         resta()
#     elif opc==3:
#         division()
#     elif opc==4:
#         multipli ()
#     else:
#         print("Adios...")
#         break
#     print("*" * 70)
#     # clear_screen()

# print('hola')

# -----------------------------------------------------------------------------------------------

menu_Carrera=("1.Atletismo","2.Ciclismo","3.Patinaje","Cualquier otro numero para salir")
desicion=("1.si", "2.no")

def crearLeerJson ():
    if not pathlib.Path("Registro.json").exists():
        with open("Registro.json","w",newline="") as file:
            contenido = json.dumps(Diccionario, indent=4)
            file.write(contenido)
        with open("Registro.json", "r") as file:
            Diccionario = json.load(file)
            print("Registro.json", "Saltó de la nube y se estrello aqui.")


def cargar_datos(Archivo):
    while True:
        global Diccionario
        try:
            with open(Archivo, "r") as file:
                Diccionario = json.load(file)
            print(Archivo, "Saltó de la nube y se estrello aqui.")
            break
        except FileNotFoundError:
            with open(Archivo, "w", newline="") as file:
                Diccionario = json.dumps(file)
            print(Archivo, "Se creo en la nube y se estrello aqui.")
            return



def guardar_Json(Diccionario,Archivo):
    try:
        contenido = json.dumps(Diccionario, indent=4)
        with open(Archivo, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")



def atletismo():
    while True:
        participante={}
        edad=int(input("Cual es la edad del participante? \n--> "))
        if edad < 18:
            print("No puedes participar en este deporte")
        else:
            print("¿Es residente de Santander?")
            for i in desicion:
                print(i)
            opc1=int(input("---> "))
            if opc1==2:
                print("No puedes participar en este deporte")
            elif opc1==1:
                print("Escriba la siguiente informacion")
                id=int(input("Numero de identificacion\n--> "))
                nombre=input("Nombre Completo\n--> ")
                telefono=int(input("Numero celular\n--> "))


            else:
                print("Error vuelva a intentar")
                return





clear_screen()
while True:
    crearLeerJson ()
    print("*" * 70)
    print("*"*14,"Menu","*"*50)
    print("*" * 70)
    print("Cual carrera desea escoger")
    print(menu_Carrera)
    for i in menu_Carrera:
        print(i)
    opc=int(input("---> "))
    if opc == 1:
        atletismo()
    elif opc ==2:
        ciclismo()
    elif opc ==3:
        patinaje()
    else:
        print("Adios...")
        break






