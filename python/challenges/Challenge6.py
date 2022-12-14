# Challenge 6

# /*
#  * Reto #6
#  * INVIRTIENDO CADENAS
#  * Fecha publicación enunciado: 07/02/22
#  * Fecha publicación resolución: 14/02/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%% Invertir str
    # for, enumerate, range
    # list comprehension
    # list // op de list
def main():
    print("Hola mundo"[::-1])
    print(invertir_string("Hola mundo"))
def invertir_string(string):
    str_invertido = ""
    n = len(string)
    idx = n-1
    while idx >= 0:
        str_invertido += string[idx]
        idx -= 1
    return str_invertido

main()