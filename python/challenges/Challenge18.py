# Challenge 18
from enum import Enum
# /*
#  * Reto #18
#  * TRES EN RAYA
#  * Fecha publicación enunciado: 02/05/22
#  * Fecha publicación resolución: 09/05/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
#  * - "X" si han ganado las "X"
#  * - "O" si han ganado los "O"
#  * - "Empate" si ha habido un empate
#  * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. 
#  * -- O si han ganado los 2. 
#  * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%% Tres en Raya
# Lista de listas -> array 2D
# tablero = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
# print(tablero) # ejemplo
class TresEnRaya(Enum):
    X = "X",
    O = "O",
    EMPTY = ""
def main():
    # Se puede ganar en fila y columna a la vez -> prop 5:4
    # Se puede ganar en una diagonal y fila/col -> prop 5:4
    # Se puede ganar en ambas diagonales -> prop 5:4
    # Pueden ganar ambos (2 filas, 2 cols)
    # Nulo -> prop no vale -> ganadores y es_tablero_valido = False
    # Empate -> ganadores [] -> es_tablero_valido = True
    # Ganadores := True, ganadores
    # Nulo := False, ganadores
    # Empate := True, []

    print("Gana X en fila y O en fila:")
    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.X, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.O],
        [TresEnRaya.O, TresEnRaya.EMPTY, TresEnRaya.X]
        ]))
    print("Gana O en col:")
    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.O],
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.X]
        ]))
    print("Gana O en línea y diagonal secundaria:")
    print(tres_en_raya([
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.O],
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X]
    ]))
    print("Gana O en col:")
    print(tres_en_raya([
        [TresEnRaya.O, TresEnRaya.EMPTY, TresEnRaya.O],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X]
    ]))
    print("Gana O en fila y col:")
    print(tres_en_raya([
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.O],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X]
    ]))
    print("Gana X en ambas diagonales:")
    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.O],
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X]
    ]))

    print("Nulo:")
    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.O, "$", TresEnRaya.O],
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.X]
        ]))
        
    print("Empate con 3 EMPTY:")
    print(tres_en_raya([
        [TresEnRaya.EMPTY, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.EMPTY, TresEnRaya.X, TresEnRaya.O],
        [TresEnRaya.EMPTY, TresEnRaya.O, TresEnRaya.X]
    ]))
    print("Empate con 1 EMPTY:")
    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.EMPTY, TresEnRaya.O],
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X]
    ]))
    # rellenar casos con mas EMPTY
def comprobar_si_hay_char_no_valido(tablero):
    contadores = [0, 0, 0]  # cont_x, cont_o, cont_empty
    chars_validos = [TresEnRaya.X, TresEnRaya.O, TresEnRaya.EMPTY]
    existe_char_no_valido = False
    for fila in tablero:
        for col in fila:
            if col not in chars_validos:
                existe_char_no_valido = True
            elif col in chars_validos:
                idx = chars_validos.index(col)
                contadores[idx] += 1
    return (existe_char_no_valido, contadores)

def comprobar_si_es_prop_correcta(tablero):
    n = len(tablero) * len(tablero[0]) # 9
    my_bool, contadores = comprobar_si_hay_char_no_valido(tablero)
    cont_x, cont_o, cont_empty = contadores
    cont_x_o = n - cont_empty
    es_proporcion_correcta = False
    if cont_x_o % 2 == 0:
        es_proporcion_correcta = cont_x_o // 2 == cont_x and cont_x_o // 2 == cont_o
    else:
        es_proporcion_correcta = abs(cont_x - cont_o) == 1
    return es_proporcion_correcta

def buscar_ganador_horizontal(tablero):
    ganadores = []
    for fila in tablero:
        cont_x, cont_o = 0, 0
        for col in fila:
            if col == TresEnRaya.EMPTY:
                continue
            elif col == TresEnRaya.X:
                cont_x += 1
                if cont_x == 3:
                    ganadores.append(TresEnRaya.X)
            else: 
                cont_o += 1
                if cont_o == 3:
                    ganadores.append(TresEnRaya.O)
    return ganadores

def buscar_ganador_vertical(tablero):
    ganadores = []
    
    for j in range(0, len(tablero[0])):
        cont_x, cont_o = 0, 0
        for i in range(0, len(tablero[0])):
            el = tablero[i][j]
            if el == TresEnRaya.EMPTY:
                continue
            elif el == TresEnRaya.X:
                cont_x += 1
                if cont_x == 3:
                    ganadores.append(TresEnRaya.X)
            else: 
                cont_o += 1
                if cont_o == 3:
                    ganadores.append(TresEnRaya.O)

    return ganadores

def buscar_ganador_linea(linea):
    cont_x, cont_o = 0, 0
    for dato in linea:
        if dato == TresEnRaya.EMPTY:
            return []
        elif dato == TresEnRaya.X:
            cont_x += 1
            if cont_x == 3:
                return [TresEnRaya.X]
        else:
            cont_o += 1
            if cont_o == 3:
                return [TresEnRaya.O]
    return []

def buscar_ganador_diagonal(tablero):
    # [1]   2   (3) --> 1 [0][0] --> (3) [0][2]
    #  4  ([5])  6  --> 5 [1][1] 
    #  (7)  8   [9] --> 9 [2][2] --> (7) [2][0]
    diagonal_principal = []
    diagonal_secundaria = []
    n = len(tablero[0])
    for i in range(n):
        diagonal_principal.append(tablero[i][i])
        diagonal_secundaria.append(tablero[i][n-1-i])
    # Pasamos bucle a una fn auxiliar
    ganador_diagonal_principal = buscar_ganador_linea(diagonal_principal)
    ganador_diagonal_secundaria = buscar_ganador_linea(diagonal_secundaria)
    return ganador_diagonal_principal + ganador_diagonal_secundaria

def tres_en_raya(tablero):
    # True el tablero no es válido - es decir, tiene chars != X, O, ""
    (existe_char_no_valido, contadores) = comprobar_si_hay_char_no_valido(tablero)
    # Proporción incorrecta de X y O
    es_proporcion_correcta = comprobar_si_es_prop_correcta(tablero)
    
    # Ganadores
    ganadores_horizontales = buscar_ganador_horizontal(tablero)
    ganadores_verticales = buscar_ganador_vertical(tablero)    
    ganadores_diagonales = buscar_ganador_diagonal(tablero)
    # Se puede ganar en fila y columna a la vez -> prop 5:4
    # Se puede ganar en una diagonal y fila/col -> prop 5:4
    # Se puede ganar en ambas diagonales -> prop 5:4
    # Pueden ganar ambos (2 filas, 2 cols)
    # Nulo -> prop no vale -> ganadores y es_tablero_valido = False
    # Empate -> ganadores [] -> es_tablero_valido = True
    ganadores = ganadores_horizontales + ganadores_verticales + ganadores_diagonales
    ganadores_set = set(ganadores)
    es_tablero_valido = not existe_char_no_valido and es_proporcion_correcta
    # Ganadores := True, ganadores
    # Nulo := False, ganadores
    # Empate := True, []
    return (es_tablero_valido, list(ganadores_set))

main()