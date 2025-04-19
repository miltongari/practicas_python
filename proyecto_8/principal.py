
from numeros import *
from os import system

def menu():
    print("\n***numero fila***")
    print("[1] - Perfumeria")
    print("[2] - Farmacia")
    print("[3] - Cosmeticos")
    print("[4] - Salir\n")

@decorar_funcion
def turno_perfumeria():
    return perfumeria

@decorar_funcion
def turno_farmacia():
    return farmacia

@decorar_funcion
def turno_cosmeticos():
    return cosmeticos

def main():
    while True:
        try:
            menu()
            select = int(input("Seleccione una opción: "))

            if select == 1:
                system("cls")
                turno_perfumeria()
            elif select == 2:
                system("cls")
                turno_farmacia()
            elif select == 3:
                system("cls")
                turno_cosmeticos()
            elif select == 4:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("Error: Ingrese un número válido")
        except TypeError:
            print("Error: error en tipo")


if __name__  == "__main__":
    main()