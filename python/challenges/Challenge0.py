# Challenge 0

# /*
#  * Reto #0
#  * EL FAMOSO "FIZZ BUZZ"
#  * Fecha publicación enunciado: 27/12/21
#  * Fecha publicación resolución: 03/01/22
#  * Dificultad: FÁCIL
#  * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%% Solución en Python
    # Complejidad
    # Como tenemos que comprobar todos los números -> Tiempo: O(n) // lineal
    # Como no tenemos que guardar mas que dos booleans por cada iteración -> Espacio: O(1) // constante
def main():
    for num in range(1,101):
        is_multiple_of_three = num % 3 == 0
        is_multiple_of_five = num % 5 == 0
        if is_multiple_of_three and is_multiple_of_five:
            print("fizzbuzz")
        elif is_multiple_of_five:
            print("buzz")
        elif is_multiple_of_three:
            print("fizz")
        else:
            print(num)
main()