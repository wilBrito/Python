

nombre = input("Como te llamas?: ")
vendido = float(input("Cuanto has vendido?: "))

comi = round(vendido*0.13,2)
print(f"{nombre} ha vendido {vendido} por lo tanto le corresponde {comi} extra")