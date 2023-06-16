class Cubo:
    def __init__(self, color):
        self.caras = 6
        self.color = color


cubo_rojo = Cubo('rojo')


class Perro:


    def ladrar(self):
        print('Guau!')


perrito = Perro()
perrito.ladrar()