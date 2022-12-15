import pytest
# Ejemplo 1 - fun que suma 1 a un número -> int
    # param -> entero
    # return -> entero
    # raise -> Exception si el param no es entero
def sumar_uno(x):
    # validar si x es entero
        # return None o Exception en caso de no int
    if isinstance(x, int):
        return int(x + 1)
    else: 
        raise Exception("El número debe ser un entero")
        
def test_sumar_uno():
    assert sumar_uno(-1) == 0
    assert sumar_uno(3) == 4
    
    # Comprobamos que se lanza una excepción si se proporciona un argumento no entero
    with pytest.raises(Exception):
        sumar_uno('hola')
    with pytest.raises(Exception):
        assert sumar_uno([1])

# Ejemplo 2 - fun que suma 1 a un número -> try / except
def sumar_uno_v2(x):
    if isinstance(x, int):
        return int(x + 1)
    else: 
        raise TypeError("El número debe ser un entero")

def test_sumar_uno_v2():
    pass

def main():
    sumar_uno(1)
    sumar_uno("Hola")   # Arroja TypeError
    sumar_uno([1])      # Arroja TypeError
# main()