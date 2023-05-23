

texto = input("Por favor ingresa un texto: ").lower()
letras = input("Ingresa 3 letras : ")
lista = texto.split()
lista.reverse()

dic = {True:'Sí',False:'No'}


print(f"""La letra {letras[0].lower()} aparece {texto.count(letras[0].lower())} veces
La letra {letras[1].lower()} aparece {texto.count(letras[1].lower())} veces
La letra {letras[2].lower()} aparece {texto.count(letras[2].lower())} veces
El texto  tiene {len(texto.split())} palabras
La primer letra del texto es {texto[0]} y la última es {texto[-1]}
Texto invertido: {' '.join(lista)}
Python esta en el texto : {dic['python' in texto]}""")

