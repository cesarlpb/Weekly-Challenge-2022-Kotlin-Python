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
tablero = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
print(tablero) # ejemplo
class TresEnRaya(Enum):
    X = "X",
    O = "O",
    EMPTY = ""
def main():
    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.O, "$", TresEnRaya.O],
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.X]
        ]))
    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.X, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.O],
        [TresEnRaya.O, TresEnRaya.EMPTY, TresEnRaya.X]
        ]))
    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.O],
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.X]
        ]))

    print(tres_en_raya([
        [TresEnRaya.EMPTY, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.EMPTY, TresEnRaya.X, TresEnRaya.O],
        [TresEnRaya.EMPTY, TresEnRaya.O, TresEnRaya.X]
    ]))

    print(tres_en_raya([
        [TresEnRaya.O, TresEnRaya.O, TresEnRaya.O],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X],
        [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X]
    ]))

    print(tres_en_raya([
        [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X],
        [TresEnRaya.X, TresEnRaya.X, TresEnRaya.O],
        [TresEnRaya.X, TresEnRaya.X, TresEnRaya.X]
    ]))
def buscar_ganador_horizontal(tablero):
    pass
def buscar_ganador_vertical(tablero):
    pass
def buscar_ganador_diagonal(tablero):
    pass
def tres_en_raya(tablero):
    # Si el tablero no es válido
    
    # Hay ganador
    # Hay empate -> no gana nadie
    # Si ganan ambos ?
    
    pass
main()
# fun main() {

#     println(checkTicTacToe([
#         [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X),
#         [TresEnRaya.O, TresEnRaya.X, TresEnRaya.O),
#         [TresEnRaya.O, TresEnRaya.O, TresEnRaya.X))))

#     println(checkTicTacToe([
#         [TresEnRaya.EMPTY, TresEnRaya.O, TresEnRaya.X),
#         [TresEnRaya.EMPTY, TresEnRaya.X, TresEnRaya.O),
#         [TresEnRaya.EMPTY, TresEnRaya.O, TresEnRaya.X))))

#     println(checkTicTacToe([
#         [TresEnRaya.O, TresEnRaya.O, TresEnRaya.O),
#         [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X),
#         [TresEnRaya.O, TresEnRaya.X, TresEnRaya.X))))

#     println(checkTicTacToe([
#         [TresEnRaya.X, TresEnRaya.O, TresEnRaya.X),
#         [TresEnRaya.X, TresEnRaya.X, TresEnRaya.O),
#         [TresEnRaya.X, TresEnRaya.X, TresEnRaya.X))))
# }

# private enum class TresEnRaya {
#     X, O, EMPTY
# }

# private enum class TicTacToeResult {
#     X, O, DRAW, NULL
# }

# private fun checkTicTacToe(board: Array<Array<TresEnRaya>>): TicTacToeResult {

#     // Null

#     if (board.count() != 3) {
#         return TicTacToeResult.NULL
#     }

#     var xCount = 0
#     var oCount = 0

#     var flatBoard: Array<TresEnRaya> = emptyArray()
#     for (row in board) {
#         flatBoard += row

#         if (row.count() != 3) {
#             return TicTacToeResult.NULL
#         }

#         for (col in row) {
#             if (col == TresEnRaya.X) {
#                 xCount += 1
#             } else if (col == TresEnRaya.O) {
#                 oCount += 1
#             }
#         }
#     }

#     if ((xCount - oCount).absoluteValue > 1) {
#         return TicTacToeResult.NULL
#     }

#     // Win or Draw

#     val winCombinations = [
#         [0, 1, 2), [3, 4, 5), [6, 7, 8), [0, 3, 6),
#         [1, 4, 7), [2, 5, 8), [0, 4, 8), [2, 4, 6))

#     var result = TicTacToeResult.DRAW

#     for (winCombination in winCombinations) {

#         if (flatBoard[winCombination[0]] != TresEnRaya.EMPTY
#                 && flatBoard[winCombination[0]] == flatBoard[winCombination[1]]
#                 && flatBoard[winCombination[0]] == flatBoard[winCombination[2]]) {

#             val winner = flatBoard[winCombination[0]]

#             if (result != TicTacToeResult.DRAW
#                     && (if (result == TicTacToeResult.O) TresEnRaya.O else TresEnRaya.X) != winner) {
#                 return TicTacToeResult.NULL
#             }

#             result = if (winner == TresEnRaya.X) TicTacToeResult.X else TicTacToeResult.O
#         }
#     }

#     return result
# }

