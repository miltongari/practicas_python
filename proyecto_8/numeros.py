
"""Generador de numeros para perfumeria"""

def generador_nump():
    num = 0
    while True:
        num += 1
        yield f"P-{num}"


"""Generador de numeros para farmacia"""

def generador_numf():
    num = 0
    while True:
        num += 1
        yield f"F-{num}"


"""Generador de numeros para cosmetico"""

def generador_numc():
    num = 0
    while True:
        num += 1
        yield f"C-{num}"


def decorar_funcion(funcion):
    def texto_formateado():
        print("Su turno es:")
        print(next(funcion()))
        print("Aguarde y seta atendido")
    return texto_formateado

perfumeria = generador_nump()
farmacia = generador_numf()
cosmeticos = generador_numc()

