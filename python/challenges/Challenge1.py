# Challenge 1
# /*
#  * Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%%
def isAnagram(word_1, word_2):
    if word_1.lower() == word_2.lower():
        return False
    return sorted(word_1) == sorted(word_2)

def main():
    print("'falso' y 'Falso':", isAnagram("falso", "Falso"))    # False
    print("'amor' y 'roma':", isAnagram("amor", "roma"))    # True
    print("'asdf' y 'qwerty':",isAnagram("asdf", "qwerty")) # False
main()