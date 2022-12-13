# Challenge 13

# /*
#  * Reto #13
#  * FACTORIAL RECURSIVO
#  * Fecha publicación enunciado: 28/03/22
#  * Fecha publicación resolución: 04/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%% Factorial
    # 5! = 5*4*3*2*1 = 120 = 5*4! = 5*4*3! ...
    # 0! = 1
    # 1! = 1
    # 3! = 3*2*1 = 6
def main():
    print("0!", factorial(0))  # 1
    print("7!", factorial(7))  # 5040
    print("10!", factorial(10)) # 3628800
    print("1!", factorial(1))  # 1    
    print("-1!", factorial(-1)) # Error o mensaje
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 0:
        return n*factorial(n-1)
    else: 
        print("n debe ser no negativo")
        return None
main()
# fun main() {
#     println(factorial(0) ?:run { "No tiene factorial" })
#     println(factorial(7) ?:run { "No tiene factorial" })
#     println(factorial(10) ?:run { "No tiene factorial" })
#     println(factorial(1) ?:run { "No tiene factorial" })
#     println(factorial(-1) ?:run { "No tiene factorial" })
# }

# private fun factorial(n: Int): Int? {
#     return if (n < 0) null else if (n <= 1) 1 else n * (factorial(n - 1)!!)
# }

