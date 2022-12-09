# Reto 2

# /*
#  * Reto #2
#  * LA SUCESIÓN DE FIBONACCI
#  * Fecha publicación enunciado: 10/01/22
#  * Fecha publicación resolución: 17/01/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
#  * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
#  * 0, 1, 1, 2, 3, 5, 8, 13...
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%% Fibonacci
    # tiempo -> 3 ops por iteración, N pasos -> O(3*N) -> O(N)
    # espacio -> 2 datos por iteración -> O(1)
def fibonacci(n):
    # La sucesión tiene sentido si n > 2
    if n > 2:
        fib_prev_prev = 0
        fib_prev = 1
        fib = 0
        for i in range(0,n+1):
            if i == 0:
                print(i, ":", fib_prev_prev)
            elif i == 1:
                print(i, ":", fib_prev)
            else:
                fib = fib_prev_prev + fib_prev
                print(i, ":", fib)
                fib_prev_prev = fib_prev
                fib_prev = fib
    else:
        return None

def main():
    fibonacci(50)
main()
#%% Alternativa mas compacta
def fib():
   n0, n1 = 0, 1
   N = 50
   for i in range(N+1):
       print(i, n0)
       n = n0 + n1
       n0, n1 = n1, n
fib()
# %%
