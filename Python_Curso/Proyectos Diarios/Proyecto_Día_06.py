import  pathlib ,os
from pathlib import Path


ruta_principal = Path('C:\\Users\wilso\Desktop\Cursos Udemy\Python\Python_Curso\Recetas')
list_categorias = []
list_receta = []

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
def programa_recetas():
    opc = 0
    while opc <= 0 or opc > 6:
        opc = int(elegir_opciones())

    match opc:
        case 1:
            categoria = elegir_categoria()
            receta = mostrar_recetas(categoria)
            leer_receta(categoria, receta)
        #case 2:

        #case 3:

        #case 4:

        #case 5:

        #case 6:




print(f'''Saludos Bienvenida
Las recetas están en {ruta_principal}
tienes {contar_recetas()} recetas''')


programa_recetas()