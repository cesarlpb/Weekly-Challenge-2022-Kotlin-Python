# Challenge 7

#
#   Reto #7
#   CONTANDO PALABRAS
#   Fecha publicación enunciado: 14/02/22
#   Fecha publicación resolución: 21/02/22
#   Dificultad: MEDIA
#  
#   Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
#   - Los signos de puntuación no forman parte de la palabra.
#   - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#   - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
#  
#   Información adicional:
#   - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#   - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#   - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#   - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  
# 
#%% 
def main():
    print(contar_palabras("Hola, mundo. Estoy programando en Python, mundo 123."))
    print(contar_palabras("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))
def contar_palabras(string):
    string_sin_signos = ""
    my_dict = {}
    for char in string:
        if char.isalnum() or char == " ":
            string_sin_signos += char
    lista = string_sin_signos.split(" ")
    for palabra in lista:
        if my_dict.get(palabra) == None:
            my_dict[palabra] = 1
        else:
            my_dict[palabra] += 1
    return my_dict
main()