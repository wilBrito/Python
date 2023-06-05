import random

vidas = 6
palabras = ["conejo", "coche", "matematicas", "miercoles", "telefono", "rojo", "azul", "java", "python"]
palabra_secreta = random.choice(palabras)


def imprimir_palabra_oculta(palabra):
    txt = "_" * len(palabra)
    return txt

def pedir_letra():
    letra = input("Introduce una letra: ")
    return letra

def validar_letra(letra_introducida, texto_secreto):
    texto_aux = ""
    bool_vidas = False

    for cont, t in enumerate(texto_secreto):

        if t == "_":
            if palabra_secreta[cont] == letra_introducida:
                texto_aux = texto_aux + letra_introducida
                bool_vidas = True
            else:
                texto_aux = texto_aux + "_"
        else:
            texto_aux = texto_aux + texto_secreto[cont]

    return texto_aux, bool_vidas

def juego_ahorcado(vidas):
    txt = imprimir_palabra_oculta(palabra_secreta)
    print(txt)

    while vidas > 0:
        letra = pedir_letra().lower()

        while len(letra) > 1:
            letra = pedir_letra().lower()

        txt_aux_2, bo = validar_letra(letra, txt)
        txt = txt_aux_2
        print(txt)

        if not bo:
            vidas -= 1

        if txt == palabra_secreta:
            break

    if vidas == 0:
        print("Fin del juego, vuelve a intentarlo")
    else:
        print("Enhorabuena")


juego_ahorcado(vidas)
