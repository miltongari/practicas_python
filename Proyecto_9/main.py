import re
from pathlib import Path
from datetime import datetime
import time

ruta = Path(Path.home(),"PycharmProjects","Proyecto_9","Mi_Gran_Directorio")
patron = r'N\D{3}-\d{5}'
archivos = []
palabras = []

def main():
    inicio = time.time()
    fecha_actual = datetime.now().strftime("%d/%m/%Y")

    for archivo in ruta.rglob("*.txt"):
        try:
            coincidencias = buscar_patron_en_archivo(patron, archivo)
            if coincidencias:
                palabras.append(coincidencias)
                archivos.append(archivo)
                print(" ")
                print(" ")
                print(" ")
                print(palabras)
                print(archivos)

        except:
            pass
    fin = time.time()
    duracion = round(fin - inicio, 2)

    # Imprimir resultado
    print("-" * 50)
    print(f"Fecha de búsqueda: {fecha_actual}\n")
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")

    for archivo, serie in zip(archivos, palabras):
        print(f"{archivo.name}\t{serie[0]}")

    print(f"\nNúmeros encontrados: {len(palabras)}")
    print(f"Duración de la búsqueda: {duracion} segundos")
    print("-" * 50)

def buscar_patron_en_archivo(patron, archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
        coincidencias = re.findall(patron, contenido)
        return coincidencias

if __name__ == "__main__":
    main()
