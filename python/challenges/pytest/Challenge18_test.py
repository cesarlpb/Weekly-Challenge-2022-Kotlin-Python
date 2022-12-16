#%% Tests de Challenge18
# Llamamos al main de Challenge18
# Necesitamos indicarle la ruta cuando está en otra carpeta
import sys
sys.path.insert(0, '/Users/cesarlpb/Code/Weekly-Challenge-2022-Kotlin-Python/python/challenges')
import Challenge18 as c # Importar en la misma carpeta
# from Challenge18 import c.TresEnRaya # Importamos solo la fn c.TresEnRaya
# Post sobre import: https://www.geeksforgeeks.org/python-import-module-from-different-directory/

def test_tres_en_raya_ganador_en_fila_debe_devolver_x():
    tablero = [
            [c.TresEnRaya.X, c.TresEnRaya.X, c.TresEnRaya.X],
            [c.TresEnRaya.O, c.TresEnRaya.X, c.TresEnRaya.O],
            [c.TresEnRaya.O, c.TresEnRaya.EMPTY, c.TresEnRaya.O]
        ]
    assert c.tres_en_raya(tablero) == (True, [c.TresEnRaya.X])
def test_tres_en_raya_ganador_en_fila_debe_devolver_o():
    pass
def test_tres_en_raya_ganador_en_fila_debe_devolver_x_o():
    pass
    # print("Gana X en fila y O en fila:")
def test_tres_en_raya_ganador_en_col_debe_devolver_o():
    pass
def test_tres_en_raya_ganador_en_diagonal_principal_debe_devolver_o():
    pass
    # print("Gana X en col y O en col:")
# [[c.TresEnRaya.X, c.TresEnRaya.X, c.TresEnRaya.X],
# [c.TresEnRaya.O, c.TresEnRaya.O, c.TresEnRaya.O],
# [c.TresEnRaya.O, c.TresEnRaya.EMPTY, c.TresEnRaya.X]]
#     # print("Gana O en col:")
# [[c.TresEnRaya.X, c.TresEnRaya.O, c.TresEnRaya.O],
# [c.TresEnRaya.X, c.TresEnRaya.O, c.TresEnRaya.X],
# [c.TresEnRaya.O, c.TresEnRaya.O, c.TresEnRaya.X]]
#     # print("Gana O en línea y diagonal secundaria:")
# [[c.TresEnRaya.O, c.TresEnRaya.O, c.TresEnRaya.O],
# [c.TresEnRaya.X, c.TresEnRaya.O, c.TresEnRaya.X],
# [c.TresEnRaya.O, c.TresEnRaya.X, c.TresEnRaya.X]]
#     # print("Gana O en col:")
# [[c.TresEnRaya.O, c.TresEnRaya.EMPTY, c.TresEnRaya.O],
# [c.TresEnRaya.O, c.TresEnRaya.X, c.TresEnRaya.X],
# [c.TresEnRaya.O, c.TresEnRaya.X, c.TresEnRaya.X]]
#     # print("Gana O en fila y col:")
# [[c.TresEnRaya.O, c.TresEnRaya.O, c.TresEnRaya.O],
# [c.TresEnRaya.O, c.TresEnRaya.X, c.TresEnRaya.X],
# [c.TresEnRaya.O, c.TresEnRaya.X, c.TresEnRaya.X]]
#     # print("Gana X en ambas diagonales:")
# [[c.TresEnRaya.X, c.TresEnRaya.O, c.TresEnRaya.X],
# [c.TresEnRaya.O, c.TresEnRaya.X, c.TresEnRaya.O],
# [c.TresEnRaya.X, c.TresEnRaya.O, c.TresEnRaya.X]]

#     # print("Nulo:")
# [[c.TresEnRaya.X, c.TresEnRaya.O, c.TresEnRaya.X],
# [c.TresEnRaya.O, "$", c.TresEnRaya.O],
# [c.TresEnRaya.O, c.TresEnRaya.O, c.TresEnRaya.X]]
        
#     # print("Empate con 3 EMPTY:")
# [[c.TresEnRaya.EMPTY, c.TresEnRaya.O, c.TresEnRaya.X],
# [c.TresEnRaya.EMPTY, c.TresEnRaya.X, c.TresEnRaya.O],
# [c.TresEnRaya.EMPTY, c.TresEnRaya.O, c.TresEnRaya.X]]
#     # print("Empate con 1 EMPTY:")
# [[c.TresEnRaya.X, c.TresEnRaya.O, c.TresEnRaya.X],
# [c.TresEnRaya.O, c.TresEnRaya.EMPTY, c.TresEnRaya.O],
# [c.TresEnRaya.X, c.TresEnRaya.O, c.TresEnRaya.X]]
    # rellenar casos con mas EMPTY

def main():
    c.main() # Llamamos a la fn main de Challenge18
# main()