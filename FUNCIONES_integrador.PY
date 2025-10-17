#script de funciones 
import csv

def Menu_opciones():  #definimos una funcion que contenga el menu de opciones
    print(''' 
          !!BIENVENIDO AL MENU DE GESTION DE PAISES!!
          1) Buscar pais por nombre
          2) Filtar paises por continentes
          3) Ordenar paises
          4) Mostar estadistica
          5) Salir 
          ''')   #la funcion se encarga de imprimir el menu
    
def cargar_paises(archivo_csv): #creo una funcion la cual leera la informacion dentro del archivo csv
    paises:list=[] #creo una lista vacia la cual se encargara de guardar la informacio
    try:
        with open (archivo_csv, mode= 'r', encoding= 'utf-8') as archivo: #use with open para abrir el archivo, y cerrarlo automaticamente
            # use encoding= utf-8 para leer los caracteres especiales dentro del csv
            lector_csv = csv.DictReader(archivo_csv,delimiter=';') #use csv.dictreader que lee el archivo y usa cada fila como diccionarios 
            for fila in lector_csv:
                try: #use try/except por si algun dato dentro del csv, no esta bien o no se puede convertir, no falle el programa
                    pais:dict={"nombre": fila["nombre"], #convertimos los valores de estadisticas a int, float
                        "poblacion": int(fila["poblacion"]),
                        "superficie": float(fila["superficie"]),
                        "continente": fila["continente"] }
                    paises.append(pais)#guardamos los datos modificados dentro de la lista
                except ValueError:
                    print("ERROR AL CONVERTIR DATOS")
        if not paises: #hacemos una vvalidacion para corrobrar que el archivo este bien y no este vacio
            print("ERROR.. el archivo esta vacio o no se oncotraron los datos esperados..")
        else:
            print(f"se cargaron {len(paises)} paises, correctamente!")
    except FileNotFoundError :
        print(f"ERROR.. no se encontro el archivo: {archivo_csv} ")

                    
                

        




    
 