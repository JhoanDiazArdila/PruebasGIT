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


def crearLeerJson ():
    global Diccionario
    Diccionario={}
    if not pathlib.Path("Registro.json").exists():
        with open("Registro.json","w",newline="") as file:
            contenido = json.dumps(Diccionario, indent=4)
            file.write(contenido)
    with open("Registro.json", "r") as file:
        Diccionario = json.load(file)
        print("Registro.json", "Saltó de la nube y se estrello aqui.")
        print("~"*100) 
        

def cargar_datos(Archivo):
    global Diccionario
    while True:
        try:
            with open(Archivo, "r") as file:
                Diccionario = json.load(file)
            print(Archivo, "Saltó de la nube y se estrello aqui.")
            break
        except FileNotFoundError:
            with open(Archivo, "w", newline="") as file:
                Diccionario = json.dumps(file)
            print(Archivo, "Se creo en la nube y se estrello aqui.")
            continue


def guardar_Json(Diccionario,Archivo):
    try:
        contenido = json.dumps(Diccionario, indent=4)
        with open(Archivo, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
        print("~"*100) 
    except Exception:
        print("Error al guardar datos")
        print("~"*100) 

# ------------------------------------------------------------------















menu_opciones=("1.Atletismo","2.Ciclismo","3.Patinaje","4.Ver Ranking","Cualquier otro numero para salir")
menu_carrera=("1.Atletismo","2.Ciclismo","3.Patinaje","Cualquier otro numero para salir")
desicion=("1.si", "2.no")

def crear_leer_json(Archivo):
    if not pathlib.Path(Archivo).exists():
        with open(Archivo, 'w') as file:
            json.dump({}, file, indent=4)
            print(Archivo, "Se creo en la nube.")
            print("~"*100) 
    with open(Archivo, 'r') as file:
        print(Archivo, "Saltó de la nube y se estrello aqui.")
        print("~"*100) 
        return json.load(file)


def guardar_JSON (Diccionario,Archivo):
    try:
        with open(Archivo, 'w') as file:
            json.dump(Diccionario, file, indent=4)
            print("Datos guardados exitosamente!!")
            print("~"*100) 
    except Exception:
        print("Error al guardar datos")
        print("~"*100) 


def id_existe_globalmente(registros, id):
    for categoria in registros.values():
        if str(id) in categoria:
            return True
    return False


def ver_posiciones():
    clear_screen()
    Archivo="Registros.json"
    registros = crear_leer_json(Archivo)
    while True:
        try:
            print("¿Cuales posiciones desea ver?")
            for i in menu_carrera:
                print(i)
            opc=int(input("--> "))
            if opc ==1:
                obtener_atletismo_top5(Archivo)
                print("*"*100)
            elif opc==2:
                obtener_ciclistas_top5(Archivo)
            elif opc==3:
                obtener_patinadores_top5(Archivo)
            else:
                print("Saliendo...")
                return
        except ValueError:
            print("Digite un valor correcto")
            continue 


def obtener_atletismo_top5(Archivo):
    registros = crear_leer_json(Archivo)
    atletismo = registros.get("Atletismo", {})
    top5 = {id: datos for id, datos in atletismo.items() if 1 <= datos["Posicion"] <= 5}
    print("Participantes en las posiciones del 1 al 5 en Atletismo:")
    print(json.dumps(top5, indent=4))

def obtener_ciclistas_top5(Archivo):
    registros = crear_leer_json(Archivo)
    ciclistas = registros.get("Ciclistas", {})
    top5 = {id: datos for id, datos in ciclistas.items() if 1 <= datos["Posicion"] <= 5}
    print("Participantes en las posiciones del 1 al 5 en Ciclistas:")
    print(json.dumps(top5, indent=4))

def obtener_patinadores_top5(Archivo):
    registros = crear_leer_json(Archivo)
    patinadores = registros.get("Patinadores", {})
    top5 = {id: datos for id, datos in patinadores.items() if 1 <= datos["Posicion"] <= 5}
    print("Participantes en las posiciones del 1 al 5 en Patinadores:")
    print(json.dumps(top5, indent=4))


def atletismo():
    clear_screen()
    Archivo="Registros.json"
    registros = crear_leer_json(Archivo)
    while True:
        try:
            participante={}
            edad=int(input("Cual es la edad del participante? \n--> "))
            if edad < 18:
                print("No puedes participar en este deporte")
                print("Saliendo...")  
                print("~"*100)
                return
            else:
                print("¿Es residente de Santander?")
                for i in desicion:
                    print(i)
                opc1=int(input("---> "))
                if opc1==2:
                    print("No puedes participar en una Carrera")
                    print("Saliendo...")  
                    print("~"*100)
                    return
                elif opc1==1:
                    print("~"*100)
                    print("Escriba la siguiente informacion")
                    id=int(input("Numero de identificacion\n--> "))
                    if id_existe_globalmente(registros,id):
                        print("Ya participo en una Carrera")
                        print("Saliendo...")
                        print("~"*100)
                        return
                    nombre=input("Nombre Completo\n--> ")
                    telefono=int(input("Numero celular\n--> "))
                    posicion=int(input("Cual es su posicion en la carrera\n--> "))
                    if "Atletismo" in registros:
                        for llave,valor in registros["Atletismo"].items():
                            if valor["Posicion"] == posicion:
                                print("posicion ya registrada en Atletismo")
                                print("Saliendo...")  
                                print("~"*100)
                                return
                    participante[id] = {
                        "Nombre":nombre,
                        "Telefono":telefono,
                        "Edad":edad,
                        "Posicion":posicion,
                        }
                    print("Estos son los datos a guardar")
                    print(participante)
                    print("~"*100) 
                    print ("¿Desea continuar y guardar?")
                    for i in desicion:
                        print(i)
                    opc1=int(input("--> "))
                    if opc1==2:
                        print("Vuelva a empezar")  
                        print("~"*100)  
                        continue
                    elif opc1==1: 
                        if "Atletismo" not in registros:
                            registros["Atletismo"] = {}
                        registros["Atletismo"].update(participante)
                        guardar_JSON (registros,Archivo)
                    else:
                        print("Digite un valor correcto")
                        continue 
                    print("¿Desea agregar otro participante a la misma carrera?")
                    for i in desicion:
                        print(i)
                    opc1=int(input("--> "))
                    if opc1==2:
                        print("Saliendo...")  
                        print("~"*100) 
                        return
                    elif opc1==1:
                        continue
                    else:
                        print("Digite un valor correcto")
                        continue
                else:
                    print("Error vuelva a intentar")
                    return
        except ValueError:
            print("Digite un valor correcto")
            continue 


def ciclismo():
    clear_screen()
    Archivo="Registros.json"
    registros = crear_leer_json(Archivo)
    while True:
        try:
            participante={}
            edad=int(input("Cual es la edad del participante? \n--> "))
            if edad < 18:
                print("No puedes participar en una Carrera")
                print("Saliendo...")  
                print("~"*100)
                return
            else:
                print("¿Es residente de Santander?")
                for i in desicion:
                    print(i)
                opc1=int(input("---> "))
                if opc1==2:
                    print("No puedes participar en una Carrera")
                    print("Saliendo...")  
                    print("~"*100)
                    return
                elif opc1==1:
                    print("~"*100)
                    print("Escriba la siguiente informacion")
                    id=int(input("Numero de identificacion\n--> "))
                    if id_existe_globalmente(registros,id):
                        print("Ya participo en una Carrera")
                        print("Saliendo...")
                        print("~"*100)
                        return
                    nombre=input("Nombre Completo\n--> ")
                    telefono=int(input("Numero celular\n--> "))
                    posicion=int(input("Cual es su posicion en la carrera\n--> "))
                    if "Ciclismo" in registros:
                        for llave,valor in registros["Ciclismo"].items():
                            if valor["Posicion"] == posicion:
                                print("posicion ya registrada en Ciclismo")
                                print("Saliendo...")  
                                print("~"*100)
                                return
                    participante[id] = {
                        "Nombre":nombre,
                        "Telefono":telefono,
                        "Edad":edad,
                        "Posicion":posicion,
                        }
                    print("Estos son los datos a guardar")
                    print(participante)
                    print("~"*100) 
                    print ("¿Desea continuar y guardar?")
                    for i in desicion:
                        print(i)
                    opc1=int(input("--> "))
                    if opc1==2:
                        print("Vuelva a empezar")  
                        print("~"*100)  
                        continue
                    elif opc1==1: 
                        if "Ciclismo" not in registros:
                            registros["Ciclismo"] = {}
                        registros["Ciclismo"].update(participante)
                        guardar_JSON (registros,Archivo)
                    else:
                        print("Digite un valor correcto")
                        continue 
                    print("¿Desea agregar otro participante a la misma carrera?")
                    for i in desicion:
                        print(i)
                    opc1=int(input("--> "))
                    if opc1==2:
                        print("Saliendo...")  
                        print("~"*100) 
                        return
                    elif opc1==1:
                        continue
                    else:
                        print("Digite un valor correcto")
                        continue
                else:
                    print("Error vuelva a intentar")
                    return
        except ValueError:
            print("Digite un valor correcto")
            continue 


def patinaje():
    clear_screen()
    Archivo="Registros.json"
    registros = crear_leer_json(Archivo)
    while True:
        try:
            participante={}
            edad=int(input("Cual es la edad del participante? \n--> "))
            if edad < 18:
                print("No puedes participar en una Carrera")
                print("Saliendo...")  
                print("~"*100)
                return
            else:
                print("¿Es residente de Santander?")
                for i in desicion:
                    print(i)
                opc1=int(input("---> "))
                if opc1==2:
                    print("No puedes participar en una Carrera")
                    print("Saliendo...")  
                    print("~"*100)
                    return
                elif opc1==1:
                    print("~"*100)
                    print("Escriba la siguiente informacion")
                    id=int(input("Numero de identificacion\n--> "))
                    if id_existe_globalmente(registros,id):
                        print("Ya participo en una Carrera")
                        print("Saliendo...")
                        print("~"*100)
                        return
                    nombre=input("Nombre Completo\n--> ")
                    telefono=int(input("Numero celular\n--> "))
                    posicion=int(input("Cual es su posicion en la carrera\n--> "))
                    if "Patinaje" in registros:
                        for llave,valor in registros["Patinaje"].items():
                            if valor["Posicion"] == posicion:
                                print("posicion ya registrada en Patinaje")
                                print("Saliendo...")  
                                print("~"*100)
                                return
                    participante[id] = {
                        "Nombre":nombre,
                        "Telefono":telefono,
                        "Edad":edad,
                        "Posicion":posicion,
                        }
                    print("Estos son los datos a guardar")
                    print(participante)
                    print("~"*100) 
                    print ("¿Desea continuar y guardar?")
                    for i in desicion:
                        print(i)
                    opc1=int(input("--> "))
                    if opc1==2:
                        print("Vuelva a empezar")  
                        print("~"*100)  
                        continue
                    elif opc1==1: 
                        if "Patinaje" not in registros:
                            registros["Patinaje"] = {}
                        registros["Patinaje"].update(participante)
                        guardar_JSON (registros,Archivo)
                    else:
                        print("Digite un valor correcto")
                        continue 
                    print("¿Desea agregar otro participante a la misma carrera?")
                    for i in desicion:
                        print(i)
                    opc1=int(input("--> "))
                    if opc1==2:
                        print("Saliendo...")  
                        print("~"*100) 
                        return
                    elif opc1==1:
                        continue
                    else:
                        print("Digite un valor correcto")
                        continue
                else:
                    print("Error vuelva a intentar")
                    return
        except ValueError:
            print("Digite un valor correcto")
            continue 





def Menu_General():
    clear_screen()
    while True:

        print("*" * 70)
        print("*"*14,"Menu","*"*50)
        print("*" * 70)
        print("¿Cual carrera desea escoger? o ¿Desea ver posiciones?")
        for i in menu_opciones:
            print(i)
        opc=int(input("---> "))
        if opc == 1:
            atletismo()
        elif opc ==2:
            ciclismo()
        elif opc ==3:
            patinaje()
        elif opc==4:
            ver_posiciones()
        else:
            print("Esta seguro?")
            for i in desicion:
                print(i)
            opc1=int(input("---> "))
            if opc1==2:
                continue
            elif opc1==1:
                print("Adios...")
                break
            else:
                print("Error vuelva a intentar")
                continue






