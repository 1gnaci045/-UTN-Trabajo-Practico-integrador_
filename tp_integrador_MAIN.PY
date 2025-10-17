import FUNCIONES_integrador as funcion

#tp integrador 
def main():
    bandera:bool=True
    while bandera:
        funcion.Menu_opciones()
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
            
        


if __name__ == "__main__":
    main()