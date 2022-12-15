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

# v3 - con validación y con try / except

def main():
    division_por_cero(1, 0)
    division_por_cero(0, 0)
main()