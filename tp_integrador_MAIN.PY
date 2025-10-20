import FUNCIONES_integrador as funcion

#tp integrador 
def main(): #definimos una funcion main, para ejecutar el script principal 
     paises = funcion.cargar_paises("paises.csv")#cargamos la informacion del csv 
     #if not paises: #hacemos una validacion en caso del que le arhivo no este bin
         #return #en caso de estar vacio el archivo, finaliza el programa antes del while 
     bandera:bool=True #creamos una variable de bool para iniciar un bucle while true
     while bandera:
         funcion.Menu_opciones() #llamamos a la funcion que muestra el menu
         decision_menu:str=input("Ingrese la opcion de desea realizar: ")
         if decision_menu == "1":
             pass
         elif decision_menu == "2":
             pass
         elif decision_menu == "3":
             pass
         elif decision_menu == "4":
             pass
         elif decision_menu == "5":
            print("CERRANDO PROGRAMA............")
            bandera:bool=False
         else:
             print("INTRODUSCA UNA OPCION VALIDA") 
         

        


if __name__ == "__main__":
    main()