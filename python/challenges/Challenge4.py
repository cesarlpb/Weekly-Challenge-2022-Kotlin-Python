# /*
#  * Reto #4
#  * ÁREA DE UN POLÍGONO
#  * Fecha publicación enunciado: 24/01/22
#  * Fecha publicación resolución: 31/01/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán:
#       - Triángulo (base * altura / 2), 
#       - Cuadrado (lado ** 2) y 
#       - Rectángulo (base * altura).
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */
#%% Polígonos
class Triangle:
    def __init__(self, _base, _height):
        self.base = _base
        self.height = _height
    def calc_area(self):
        return round(self.base * self.height / 2, 2)
    def __str__(self):
        return f"Base: {self.base} u, Altura: {self.height} u. Área: {self.calc_area()} u^2"

class Square:
    pass
class Rectangle:
    pass

def main():
    triangle = Triangle(3,4)    # 6
    # square = Square(3)          # 9
    # rectangle = Rectangle(3,4)  # 12
main()