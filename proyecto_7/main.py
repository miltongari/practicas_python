from os import system,sys

class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self,deposito):
        self.balance += deposito
        print("Deposito aceptado")

    def retirar(self, retiro):
        if self.balance >= retiro:
            self.balance -= retiro
            print("retiro realizado")
        else:
            print("Sin saldo suficiente")



def crear_cliente():
    nombre_cliente = input("nombre: ")
    apellido_cliente = input("apellido: ")
    numero_cuenta = input("numero de cuenta: ")
    cliente = Cliente(nombre_cliente,apellido_cliente,numero_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    system("cls")
    print(mi_cliente)
    while True:
        opcion = int(input("""
        [1] - Depositar
        [2] - Retirar
        [3] - Salir
        """))
        match opcion:
            case 1:
                system("cls")
                monto_dep = int(input("Deposito: "))
                mi_cliente.depositar(monto_dep)
            case 2:
                system("cls")
                monto_ret = int(input("Retiro: "))
                mi_cliente.retirar(monto_ret)
            case 3:
                sys.exit(1)
            case _:
                system("cls")
                print("Numero invalido")

inicio()