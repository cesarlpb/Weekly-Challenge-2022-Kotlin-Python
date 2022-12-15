# Challenge 17
from enum import Enum
# /*
#  * Reto #17
#  * LA CARRERA DE OBSTÁCULOS
#  * Fecha publicación enunciado: 25/04/22
#  * Fecha publicación resolución: 02/05/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
#  *        variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%% Carrera de obstáculos

class Acciones(Enum):
    RUN = "_",
    JUMP = "|"

# Prints de ejemplo:
# print(Acciones.RUN)
# print(Acciones.RUN.name)
# print(Acciones.RUN.value)

# Comparación de _ con valor de RUN: 

# print(Acciones.RUN.value[0], "_")     # _ _
# print(Acciones.RUN.value[0] == "_")   # True
# print(type(Acciones.RUN.value[0]), type("_")) # str
def main():
    print(verificar_carrera([Acciones.RUN, Acciones.JUMP, Acciones.RUN, Acciones.JUMP, Acciones.RUN], "_|_|_"))
    print(verificar_carrera([Acciones.RUN, Acciones.RUN, Acciones.RUN, Acciones.JUMP, Acciones.RUN], "_|_|_"))
    print(verificar_carrera([Acciones.RUN, Acciones.RUN, Acciones.JUMP, Acciones.JUMP, Acciones.RUN], "_|_|_"))
    print(verificar_carrera([Acciones.JUMP, Acciones.RUN, Acciones.JUMP, Acciones.JUMP, Acciones.RUN], "_|_|_|_"))
    print(verificar_carrera([Acciones.RUN, Acciones.JUMP, Acciones.RUN, Acciones.JUMP], "_|_|_"))
    print(verificar_carrera([Acciones.RUN, Acciones.JUMP, Acciones.RUN, Acciones.JUMP, Acciones.RUN, Acciones.JUMP, Acciones.RUN], "_|_|_"))
    print(verificar_carrera([Acciones.JUMP, Acciones.JUMP, Acciones.JUMP, Acciones.JUMP, Acciones.JUMP], "|||||"))
    print(verificar_carrera([Acciones.JUMP, Acciones.JUMP, Acciones.JUMP, Acciones.JUMP, Acciones.JUMP], "||?||"))


def verificar_carrera(acciones, carrera):
    # Verificamos que los chars de carrera sean "_" y "|"
    for elemento in carrera:
        if elemento not in (Acciones.JUMP.value[0], Acciones.RUN.value[0]):
            return (carrera, "", False)
    # Iteramos en acciones y carrera para comprobar si el atleta realiza las acciones correctas:
    carrera_mod = ""
    for accion, elemento in zip(acciones, carrera):
        if accion.value[0] != elemento:
            if accion == Acciones.RUN and elemento == "|":
                carrera_mod += "/"
                return (carrera, carrera_mod, False)
            elif accion == Acciones.JUMP and elemento == "_":
                carrera_mod += "x"
                return (carrera, carrera_mod, False)
        else:
            carrera_mod += elemento
    
    return (carrera, carrera_mod, len(acciones) == len(carrera))

main()