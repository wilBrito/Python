import  pathlib ,os
from pathlib import Path



ruta_principal = Path('C:\\Users\wilso\Desktop\Cursos Udemy\Python\Python_Curso\Recetas')
list_categorias = []
list_receta = []
finalizado = False

def contar_recetas():
    initial_count = 0
    for path in ruta_principal.iterdir():
        for aux in path.iterdir():
            if aux.is_file():
                initial_count += 1
    return initial_count

def elegir_opciones():
    opcion = input('''_______________________
[1] Leer Receta
[2] Crear Receta
[3] Crear Categoría
[4] Eliminar Receta
[5] Eliminar Categoría
[6] Finalizar Programa
Selecciona una opción: ''')
    return opcion

def elegir_categoria():
    cont = 0
    opcion = 0
    print("__________________________")
    for i, path in enumerate(ruta_principal.iterdir()):
        print(f"[{i+1}] {os.path.basename(path)}")
        list_categorias.append(os.path.basename(path))
        cont += 1
    while opcion <= 0 or opcion > cont:
        opcion = int(input("Elige una categoria: "))

    return opcion

def eliminar_categoria(categoria):
    os.rmdir(ruta_principal / list_categorias[categoria - 1])

def mostrar_recetas(categoria_seleccionada):
    path = ruta_principal / list_categorias[categoria_seleccionada - 1]
    opcion = 0
    cont = 0
    print("__________________________")
    for i, p in enumerate(path.iterdir()):
        print(f"[{i+1}] {os.path.basename((p))}")
        list_receta.append(os.path.basename((p)))
        cont += 1

    while opcion <= 0 or opcion > cont:
        opcion = int(input("Elige una receta para leer: "))

    return opcion

def leer_receta(categoria_seleccionada,receta_seleccionada):
    print("__________________________")
    path = ruta_principal / list_categorias[categoria_seleccionada - 1] / list_receta[receta_seleccionada - 1]
    archivo = open(path, 'r')
    print(archivo.read())
    archivo.close()

def eliminar_receta(categoria,receta):
    os.remove(ruta_principal / list_categorias[categoria - 1] / list_receta[receta - 1])

def nombre_contenido_receta():
    print("__________________________")
    nombre = input("Escribe un nombre: ") + ".txt"
    contenido = input("Escribe su contenido: ")
    return nombre, contenido

def crear_receta(categoria, nombre, contenido):
    print("__________________________")
    path = ruta_principal / list_categorias[categoria - 1] / nombre
    archivo = open(path, 'a')
    archivo.write(contenido)
    archivo.close()


def nombre_categoria():
    print("__________________________")
    categoria = input("Escribe un nombre: ")
    return  categoria

def crear_categoria(nombre):
    os.mkdir(ruta_principal / nombre)



def programa_recetas():
    opc = 0
    while opc <= 0 or opc > 6:
        os.system('cls')
        opc = int(elegir_opciones())

    match opc:
        case 1:
            categoria = elegir_categoria()
            receta = mostrar_recetas(categoria)
            leer_receta(categoria, receta)
        case 2:
            categoria = elegir_categoria()
            nombre, contenido = nombre_contenido_receta()
            crear_receta(categoria, nombre, contenido)
        case 3:
            nombre = nombre_categoria()
            crear_categoria(nombre)
        case 4:
            categoria = elegir_categoria()
            receta = mostrar_recetas(categoria)
            eliminar_receta(categoria,receta)
        case 5:
            categoria = elegir_categoria()
            eliminar_categoria(categoria)
        case 6:
            finalizado = True
            return finalizado



print(f'''Saludos Bienvenida
Las recetas están en {ruta_principal}
tienes {contar_recetas()} recetas''')


while not finalizado:
    finalizado = programa_recetas()