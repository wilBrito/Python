import  pathlib ,os
from pathlib import Path


ruta_principal = Path('C:\\Users\wilso\Desktop\Cursos Udemy\Python\Python_Curso\Recetas')

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
        cont += 1

    while opcion <= 0 or opcion > cont:
        opcion = int(input("Elige una categoria: "))

    return opcion

#def leer_receta():



def programa_recetas():
    opc = 0
    while opc <= 0 or opc > 6:
        opc = int(elegir_opciones())

    match opc:
        case 1:
            categoria = elegir_categoria()
        #case 2:

        #case 3:

        #case 4:

        #case 5:

        #case 6:




print(f'''Saludos Bienvenida
Las recetas están en {ruta_principal}
tienes {contar_recetas()} recetas''')


programa_recetas()