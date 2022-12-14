# Challenge 12

# /*
#  * Reto #12
#  * ¿ES UN PALÍNDROMO?
#  * Fecha publicación enunciado: 21/03/22
#  * Fecha publicación resolución: 28/03/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */
#%% Determinar si un texto es palíndromo
def main():
    print(es_palindromo("Ana lleva al oso la avellana."))       # True
    print(es_palindromo("Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida")) # True
    print(es_palindromo("¿Qué os ha parecido el reto?"))        # False
def es_palindromo(string):
    from unidecode import unidecode

    str_sin_signos = ""
    for char in string.replace(" ", ""):
        if char.isalnum():
            str_sin_signos += char.lower()
    # Aplicamos unidecode para quitar acentos y chars fuera del alfabeto inglés
    str_sin_signos = unidecode(str_sin_signos)    
    n = len(str_sin_signos)
    for idx, char in enumerate(str_sin_signos):
        if not char == str_sin_signos[n-idx-1]:
            return False
    return True
main()