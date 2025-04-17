from pathlib import Path
from os import system, sys
import os
ruta = Path(Path.home(),"Documents","Python", "proyecto del dia 6", "Recetas")



def main ():
    while True:
        print(f"numero de recetas encontradas: {contar_recetas()}")
        menu()
        select = int(input("Selecciona un numero: "))
        system("cls")
        seleccion(select)


def contar_recetas():
    count = 0
    for txt in Path(ruta).glob("**/*.txt"):
        count += 1

    return count


def menu ():
    print("""
    [1] - leer receta
    [2] - crear receta
    [3] - crear categoria
    [4] - eliminar categoria
    [5] - finalizar programa
    """
    )


def seleccion (num):
    match  num:
        case 1: 
            system("cls")
            count = 0
            carpetas = leer_receta()
            system("cls")
            for element in carpetas:
                count += 1
                print(f"{count}: {element}")
            select = int(input("Seleciona una carpeta: "))
            guia = Path(ruta, carpetas[select - 1])
            archivos_txt_direccion = list(guia.glob("*.txt"))
            archivos_txt = [archivo.name for archivo in guia.glob("*.txt")]

            count = 0
            system("cls")
            for element in archivos_txt:
                count += 1
                print(f"{count}: {element}")
            select = int(input("Seleciona un: "))
            with open(archivos_txt_direccion[select - 1], 'r') as lectura:
                contenido = lectura.read()
                system("cls")
                print(contenido)
            input("Presiona Enter para continuar al menu principal...")
            system("cls")

        case 2:
            # select = int()
            system("cls")
            count = 0
            carpetas = leer_receta()
            system("cls")
            for element in carpetas:
                count += 1
                print(f"{count}: {element}")
            select = int(input("Donde va a crear su receta: "))
            guia = Path(ruta / carpetas[select - 1])
            system("cls")
            nombre_receta = input("Dame el nombre de la receta: ")
            receta = input("Contenido de la receta: ")
            
            #concatena la ruta con el nombre del archivo
            ruta_archivo = guia / f"{nombre_receta}.txt"
            with open(ruta_archivo, "w") as archivo:
                archivo.write(receta)
            input("Presiona Enter para continuar al menu principal...")
            system("cls")



        case 3:
            system("cls")
            select = input("seleccione la categoria que quiere crear: ")
            os.makedirs(Path(ruta, select))
            system("cls")
            print(f"Categoria \"{select}\" fue creada")
            input("Presiona Enter para continuar al menu principal...")
            system("cls")


        case 4:
            system("cls")
            count = 0
            carpetas = leer_receta()
            system("cls")
            for element in carpetas:
                count += 1
                print(f"{count}: {element}")
            select = int(input("que categoria va a eliminar: "))
            os.rmdir(Path(ruta / carpetas[select - 1]))
            system("cls")
            print(f"Categoria \"{carpetas[select - 1]}\" eliminada")
            input("Presiona Enter para continuar al menu principal...")
            system("cls")


        case 5:
            sys.exit(1)
        case _:
            return "Numero Invalido"

def leer_receta():
    directorio = Path(ruta)
    carpetas = [carpeta.name for carpeta in directorio.iterdir() if carpeta.is_dir()]
    return carpetas



if __name__ == "__main__":
    main()