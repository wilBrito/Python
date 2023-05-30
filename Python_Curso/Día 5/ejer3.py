def ejer(*args):
    aux = 1


    for numero in args:
        if aux == 0 and numero == 0:
            return True
        else:
            aux = numero
            pass
    return False


print(ejer(5,6,1,0,8,9,3,5))