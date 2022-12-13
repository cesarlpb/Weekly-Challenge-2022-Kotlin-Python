# Challenge 14

# /*
#  * Reto #14
#  * ¿ES UN NÚMERO DE ARMSTRONG?
#  * Fecha publicación enunciado: 04/04/22
#  * Fecha publicación resolución: 11/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
#  * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
#  *

### Número de Armstrong:
# Un número de Armstrong (AKA Plus Perfect number, o número narcisista) es un número que es igual a la suma de la nenésima potencia de los dígitos, donde nes el número de dígitos del número.

# Por ejemplo, 153 tiene 3 dígitos y 153 = 1^3 + 5^3 + 3^3, por 153 lo tanto, es un número de Armstrong.

# Por ejemplo, 8208 tiene 4 dígitos y 8208 = 8^4 + 2^4 + 0^4 + 8^4, por 8208 lo tanto, es un número de Armstrong.
###

#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

# fun main() {
#     println(isArmstrong(371))
#     println(isArmstrong(-371))
#     println(isArmstrong(372))
#     println(isArmstrong(0))
# }

# private fun isArmstrong(number: Int): Boolean {

#     return if (number < 0) {
#         false
#     } else {
#         var sum = 0
#         val powValue = number.toString().length

#         number.toString().forEach { character ->
#             sum += character.toString().toDouble().pow(powValue).toInt()
#         }

#         number == sum
#     }
# }