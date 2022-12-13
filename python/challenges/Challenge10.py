# Challenge10

# /*
#  * Reto #10
#  * EXPRESIONES EQUILIBRADAS
#  * Fecha publicación enunciado: 07/03/22
#  * Fecha publicación resolución: 14/03/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cierran en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%% Verificamos si los str tienen (), [], {} bien cerrados
def main():
    # print(es_str_equilibrado("{a + b [c] * (2x2)}}}}"))                 # False
    # print(es_str_equilibrado("{ [ a * ( c + d ) ] - 5 }"))              # True
    # print(es_str_equilibrado("{ a * ( c + d ) ] - 5 }"))                # False
    # print(es_str_equilibrado("{a^4 + (((ax4)}"))                        # False
    print(es_str_equilibrado("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))   # False - pos
    # print(es_str_equilibrado("{{{{{{(}}}}}}"))                          # False
    # print(es_str_equilibrado("(a"))                                     # False
def es_str_equilibrado(string):
    chars_validos = "{}()[]"
    cuenta_chars = {}
    # Añadimos caracteres válidos al dict
    for char_valido in chars_validos:
        cuenta_chars[char_valido] = 0
    
    # Hacemos copia del dict y cambiamos values a []
    posiciones_char = cuenta_chars.copy()
    for key in posiciones_char.keys():
        posiciones_char[key] = []

    lista = [char if char in chars_validos else "" for char in string]
    input_str = "".join(lista)
    for char in input_str:
        cuenta_chars[char] += 1
    # Verificamos cuentas de (), {}, []
    n = len(chars_validos) # debe ser par
    for idx in range(int(n/2)):
        cuenta_izq = cuenta_chars.get(chars_validos[idx])
        cuenta_der = cuenta_chars.get(chars_validos[n-idx-1])
        if cuenta_izq != cuenta_der:
            return False
    # Verificamos posiciones de (), {}, []
    for idx in range(len(input_str)):
        caracter = input_str[idx]
        posiciones_char[caracter].append(idx)
    # TODO: Queda terminar la verificacion de si las posiciones son correctas
    print(posiciones_char)
    return True
main()
# fun main() {
#     println(isBalanced("{a + b [c] * (2x2)}}}}"))
#     println(isBalanced("{ [ a * ( c + d ) ] - 5 }"))
#     println(isBalanced("{ a * ( c + d ) ] - 5 }"))
#     println(isBalanced("{a^4 + (((ax4)}"))
#     println(isBalanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))
#     println(isBalanced("{{{{{{(}}}}}}"))
#     println(isBalanced("(a"))
# }

# private fun isBalanced(expression: String): Boolean {

#     val symbols = mapOf("{" to "}", "[" to "]", "(" to ")")
#     val stack = arrayListOf<String>()

#     expression.forEach {

#         val symbol = it.toString()
#         val containsKey = symbols.containsKey(symbol)

#         if (containsKey || symbols.containsValue(symbol)) {
#             if (containsKey) {
#                 stack.add(symbol)
#             } else if (stack.isEmpty() || symbol != symbols[stack.removeLast()]) {
#                 return false
#             }
#         }
#     }

#     return stack.isEmpty()
# }