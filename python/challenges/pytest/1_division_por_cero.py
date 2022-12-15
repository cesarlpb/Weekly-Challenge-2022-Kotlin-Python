#%% Tests de división por cero
import pytest 

# v1 - sin validación y sin try / except
def division_por_cero(x, y):
    # No hemos validado que x e y sean números
        # Ni que y != 0
    return x / y

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        division_por_cero(1, 0)
    with pytest.raises(ZeroDivisionError):
        division_por_cero(0, 0)

# v2 - con validación y sin try / except
    # Suponemos x e y son números enteros -> int
def division_por_cero_v2(x, y):
    if isinstance(x, int) == False or isinstance(y, int) == False:
        raise TypeError("x e y deben ser números")
    elif y == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return x / y # en general es float
def test_division_por_cero_v2():
    assert division_por_cero_v2(1, 1) == 1
    assert division_por_cero_v2(5, 2) == 5/2
    assert division_por_cero_v2(1, 3) == 1/3
    with pytest.raises(TypeError):
        division_por_cero_v2("1", 3)
    with pytest.raises(TypeError):
        division_por_cero_v2(1, "3")
    with pytest.raises(ZeroDivisionError):
        division_por_cero_v2(1, 0)
# v3 - con validación y con try / except
def division_por_cero_v3(x, y):
    try:
        if isinstance(x, int) == False or isinstance(y, int) == False:
            raise TypeError("x e y deben ser números")
        elif y == 0:
            raise ZeroDivisionError("No se puede dividir entre 0")
        return x / y # en general es float
    except TypeError as e:
        print("Ha ocurrido este error:", e)
    except ZeroDivisionError as e:
        print("Ha ocurrido este error:", e)
def test_division_por_cero_v3():
    assert division_por_cero_v3(1, 1) == 1
    assert division_por_cero_v3(5, 2) == 5/2
    assert division_por_cero_v3(1, 3) == 1/3
    assert division_por_cero_v3("1", 3) == None
    assert division_por_cero_v3(1, "3") == None
    assert division_por_cero_v3(1, 0) == None
def main():
    division_por_cero(1, 0)
    division_por_cero(0, 0)
    division_por_cero_v2(1, 0)
    division_por_cero_v2(0, 0)
    division_por_cero_v3(1, 0)
    division_por_cero_v3(0, 0)
    division_por_cero_v3("1", 3)
    division_por_cero_v3(1, "3")
# main()