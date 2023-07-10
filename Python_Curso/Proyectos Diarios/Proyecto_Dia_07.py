


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def imprimir_cliente(self):
        print(f"""          
        {self.nombre} {self.apellido}
        Número de cuenta: {self.numero_cuenta}
        Balance: {self.balance}
        """)

    def depositar(self):
        deposito = input("Cuanto dinero quieres depositar en tu cuenta: ")
        self.balance = str(int(self.balance) + int(deposito))


    def retirar(self):
        retiro = input("Cuanto dinero quieres retirar en tu cuenta: ")
        if int(retiro) < int(self.balance):
            self.balance = str(int(self.balance) - int(retiro))
        else:
            print("No tienes suficiente saldo")



def crear_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = input("Número Cuenta: ")
    balance = int(input("Balance: "))

    cliente = Cliente(nombre, apellido, numero_cuenta, balance)

    return cliente

def acciones_banco():

    opc = input("""
        [1] Depositar
        [2] Retirar
        [3] Salir
        Elige una opción: """)
    return int(opc)



def inicio():
    cliente = crear_cliente()
    aux = True
    while aux:
        cliente.imprimir_cliente()
        opc = acciones_banco()
        while opc > 3 and opc < 1:
            opc = acciones_banco()

        match opc:
            case 1:
                cliente.depositar()
            case 2:
                cliente.retirar()
            case 3:
                aux = False




inicio()