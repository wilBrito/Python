
lista = [0, 0, 0]

def panel():
    opc = input("""
        [1] Perfumería
        [2} Farmacia
        [3] Cosmética
        [4] Salir
        Elija un área: """)
    return int(opc)

def imprimir_turno(letra, numero):
    print(f"""
        Su turno es:
            {letra}-{numero}
    Aguarde será atendido
    """)




def inicio():
    aux = True
    while aux:
        opc = panel()
        while opc not in range(1,5):
            opc = panel()

        match opc:
            case 1:
                lista[0] += 1
                imprimir_turno('P', lista[0])
            case 2:
                lista[1] += 1
                imprimir_turno('F', lista[1])
            case 3:
                lista[2] += 1
                imprimir_turno('C', lista[2])
            case 4:
                aux = False




inicio()