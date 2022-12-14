# Challenge 16

# /*
#  * Reto #16
#  * EN MAYÚSCULA
#  * Fecha publicación enunciado: 18/04/22
#  * Fecha publicación resolución: 25/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */
#%% Pasar palabras a la primera letra en mayúsculas
def main():
    print(capitalizar_palabras("¿hola qué tal estás?"))
    print(capitalizar_palabras("¿hola      qué tal estás?"))
    print(capitalizar_palabras("El niño ñoño"))
def capitalizar_palabras(string):
    lista = string.split(" ")
    # Idea: expandir para más caracteres iniciales no válidos
        # considerar varios al inicio como #$%&...
        # considerar que puedan aparecer en medio del string
    primer_char = lista[0][0]
    chars_a_descartar = "¿¡#"
    if primer_char in chars_a_descartar:
        lista[0] = lista[0][1:]
    else: 
        primer_char = ""
    string_capitalizado = [palabra.capitalize() for palabra in lista if palabra != ""]
    return primer_char + " ".join(string_capitalizado)
main()