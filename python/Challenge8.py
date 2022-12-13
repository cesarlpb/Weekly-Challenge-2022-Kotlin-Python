# Challenge 8

#
#   Reto #8
#   DECIMAL A BINARIO
#   Fecha publicación enunciado: 18/02/22
#   Fecha publicación resolución: 02/03/22
#   Dificultad: FÁCIL
#  
#   Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  
#   Información adicional:
#   - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#   - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#   - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#   - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  
# 

# Decimal a binario
# 0 y 1

# 10 -> 1010 en binario
# Decimal (base 10): 0..9 -> 10 = 1*10^1 + 0*10^0
# 1503 -> 1*10^3 + 5*10^2 + 0*10 + 3*10^0

# Binario => 1010 = 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = 8 + 2 = 10
# 125 => 1111101 = 1*2^6 + 1*2^5 + 1*2^4 + 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 125
#%% main
def main():
    print("10 en binario:", int_a_binario(10))   # 1010
    print("125 en binario:", int_a_binario(125)) # 1111101

    print("125.25 en binario:", float_a_binario(125.25)) # 1111101.01
    print("125.5 en binario:", float_a_binario(125.5)) # 1111101.1
    print("125.1 en binario:", float_a_binario(125.1)) # 1111101.??????
    # print("125.75 en binario:", float_a_binario(125.75)) # 1111101.11
def int_a_binario(entero):
    cociente = int(entero)
    str_binario = ""
    while cociente > 0:
        str_binario += str(cociente % 2)
        cociente = cociente // 2
    return str_binario[::-1].encode('utf-8')
def float_a_binario(num):
    exp = 0
    my_num = num
    
    while not my_num.is_integer() and exp < 10:
        exp += 1
        my_num = num * 2**exp

    my_str = int_a_binario(my_num).decode('utf-8')
    my_str = my_str[:-exp] + "." +my_str[-exp:]
    return (my_str, exp)
main()