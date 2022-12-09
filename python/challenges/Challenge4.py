# Reto 4
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
#%% Polígonos - Triángulo, Cuadrado, Rectángulo
    # tiempo y espacio -> O(1)
class Triangle:
    def __init__(self, _base, _height):
        self.name = "Triángulo".center(20)
        self.base = _base
        self.height = _height
    def calc_area(self):
        return round(self.base * self.height / 2, 2)
    def __str__(self):
        return f"Polígono:{self.name}\nBase: {self.base} u, Altura: {self.height} u. Área: {self.calc_area()} u^2"

class Square:
    def __init__(self, _side):
        self.name = "Cuadrado".center(20)
        self.side = _side
    def calc_area(self):
        return round(self.side ** 2, 2)
    def __str__(self):
        return f"Polígono:{self.name}\nLado: {self.side} u. Área: {self.calc_area()} u^2"

class Rectangle:
    def __init__(self, _base, _height):
        self.name = "Rectángulo".center(20)
        self.base = _base
        self.height = _height
    def calc_area(self):
        return round(self.base * self.height, 2)
    def __str__(self):
        return f"Polígono:{self.name}\nBase: {self.base} u, Altura: {self.height} u. Área: {self.calc_area()} u^2"

def main():
    triangle = Triangle(3,4)    # 6
    square = Square(3)          # 9
    rectangle = Rectangle(3,4)  # 12
    print(triangle)
    print(square)
    print(rectangle)
main()
# Futuros cambios
    # Crear una clase Polygon y derivar las clases Triangle, Square, Rectangle de ésta
    # Hacer override del método de cálculo del área
    # Extender a cualquier tipo de polígono regular
        # https://es.wikihow.com/calcular-el-%C3%A1rea-de-un-pol%C3%ADgono
        # A = 1/2 * perimetro * apotema
            # Triángulo -> "perimetro" es base // apotema es altura
            # Cuadrado como 4 triángulos -> 1/2 * 4 * lado * 1/2 * lado = lado * lado
            # Rectángulo no es "regular", son dos lados distintos
        # Perímetro = la suma de las longitudes de todos los lados
        # Apotema = un segmento que une el centro del polígono con el punto medio de cualquier lado perpendicular a dicho lado