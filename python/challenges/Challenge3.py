# /*
#  * Reto #3
#  * ¿ES UN NÚMERO PRIMO?
#  * Fecha publicación enunciado: 17/01/22
#  * Fecha publicación resolución: 24/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */
#%% isPrime
    # primo := solo es divisible por sí mismo y 1 -> Ej: 1, 2, 3, 5, 7, 11, 13 ...
    # no primo := tiene divisores distintos de sí mismo y 1 -> Ej: 4, 6, 8, 10, 12 ...
# Complejidad
    # tiempo -> N * N / 2 -> O(N^2)
    # espacio -> O(1)

def isPrime(num):
    for divisor in range(2,num // 2 + 1):
        if num % divisor == 0:
            return False
    return True

def main():
    N = 100
    for i in range(1,N+1):
        if isPrime(i):
            print(i)
main()

# Posibles mejoras
    # Descartar los números pares porque salvo el 2, son divisibles por 2 => no primos
    # Números que terminan en 5 o 0 -> descartados por ser divisible por 5 o 10 respectivamente
    # Suma de los dígitos es múltiplo de 3 o 9 -> divisible por 3 o 9
    # Etc.
# Algunas reglas de divisibilidad que se podrían implementar:
    # Un número entero es divisible por 2 si su último dígito es 0, 2, 4, 6 o 8.
    # Un número entero es divisible por 3 si la suma de sus dígitos es divisible por 3.
    # Un número entero es divisible por 4 si el número formado por sus dos últimos dígitos es divisible por 4.
    # Un número entero es divisible por 5 si su último dígito es 0 o 5.
    # Un número entero es divisible por 6 si es divisible por 2 y 3.
    # Un número entero es divisible por 9 si la suma de sus dígitos es divisible por 9.
    # Un número entero es divisible por 10 si su último dígito es 0.
    # Un número entero es divisible por 11 si la diferencia entre la suma de los dígitos en las posiciones pares y la suma de los dígitos en las posiciones impares es divisible por 11.