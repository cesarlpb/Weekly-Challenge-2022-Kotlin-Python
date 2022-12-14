# Challenge 15
import math
# /*
#  * Reto #15
#  * ¿CUÁNTOS DÍAS?
#  * Fecha publicación enunciado: 11/04/22
#  * Fecha publicación resolución: 18/04/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
#  * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  * - La función recibirá dos String y retornará un Int.
#  * - La diferencia en días será absoluta (no importa el orden de las fechas).
#  * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%% Cálculo de diferencia de fechas
def main():    

    # Año bisiesto - ok
    # print(es_año_bisiesto(2000)) # True
    # print(es_año_bisiesto(2022)) # False
    # print(es_año_bisiesto(2020)) # True

    # calc_dia_absoluto() - ok
    # dias_en_cada_mes = {
    #     1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 
    #     6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
    #     11: 30, 12: 31 
    # }
    # dias_mes = list(dias_en_cada_mes.values())
    # print(calc_dia_absoluto(10, 1, 2022, dias_mes)) # 10
    # print(calc_dia_absoluto(1, 3, 2020, dias_mes))  # 61
    # Sin datetime
    # ok
    print("Días entre 14/2/2020 y 14/02/2023", calc_dias("14/2/2020", "14/02/2023"))    # 365*3 + 1 -> delta_1
    print("Días entre 14/2/2019 y 14/02/2023", calc_dias("14/2/2019", "14/02/2023"))    # 365*4 + 1 -> delta_2
    print("Días entre 14/2/2021 y 14/03/2024", calc_dias("14/2/2021", "14/03/2024"))    # 365*3 + 29 -> delta_2

    # Test - grupo 2 - ok
    print(calc_dias("14/12/2022", "10/01/2023"))    # 27 días
    print(calc_dias("14/12/2022", "10/02/2023"))    # 58 días
    print(calc_dias("14/12/2022", "10/03/2023"))    # 58+28 = 86 días
    print(calc_dias("18/05/2022", "29/05/2023"))    # 376 días
    print(calc_dias("18/05/2022", "29/05/2022"))    # 11 días
    print(calc_dias("18/5/2022", "29/04/2022"))     # 19 días
    # print(calc_dias("hola, mundo", "29/04/2022"))   # Error
    
    # Con datetime
    str_d1 = '20/10/2021'
    str_d2 = '20/2/2022'
    # print(str_d2, "-", str_d1, ":", calc_dias_datetime(str_d1, str_d2))
    # Test
    print(calc_dias_datetime("18/05/2022", "29/05/2023"))
    print(calc_dias_datetime("18/05/2022", "29/05/2022"))
    print(calc_dias_datetime("18/5/2022", "29/04/2022"))
    print(calc_dias_datetime("asdf", "29/04/2022"))         # Error

def str_es_int(string):
    try: 
        if isinstance(int(string), int):
            return True
    except ValueError:
        return False

def encontrar_datos_erroneos(str1, str2):
        lista1 = str1.split("/")
        lista2 = str2.split("/")
        datos_erroneos = []
        if sum([str_es_int(digito) for digito in lista1]) < 3:
            datos_erroneos.append(str1)
        if sum([str_es_int(digito) for digito in lista2]) < 3:
            datos_erroneos.append(str2)
        return datos_erroneos

def calc_dias_datetime(date1, date2):
    from datetime import datetime
    # Convertimos strings en obj datetime
        # Añadimos bloque try / except
    try:
        d1 = datetime.strptime(date1, "%d/%m/%Y")
        d2 = datetime.strptime(date2, "%d/%m/%Y")
    except ValueError:
        dato_erroneo = encontrar_datos_erroneos(date1, date2)
        print(f"Error: El input {dato_erroneo} no tiene el formato de fecha correcto: dd/mm/aaaa")
    else:
        # Calculamos diferencia de fechas en timedelta
        delta = d2 - d1
        return f'Han pasado {delta.days} días'
    finally: 
        return "No se pudo calcular la diferencia de días"
    
def es_año_bisiesto(año):
    # si el año es bisiesto, Feb tiene 29 días
    # Año bisiesto := Año bisiesto es el divisible entre 4, salvo que sea año secular -último de cada siglo, 
    # terminado en «00»-, en cuyo caso también ha de ser divisible entre 400.
        # "dia_absoluto" := del 1 al 365 o 366
    if not año % 4:
        if año % 100:
            return True
        elif not año % 100 and not año % 400:
            return True
    return False

def calc_dia_absoluto(dia, mes, año, dias_mes):
    # 10, 1, 2022 -> no bis -> 10
    # 1, 3, 2020 -> bisiesto -> 31 + 29 + 1 = 61
    # 14, 12, yyyy -> suma hasta nov
    dia_absoluto = 0
    dia_bisiesto = 0
    mes_while = 1
    while mes_while < mes:        
        dia_absoluto += dias_mes[mes_while-1]
        if mes_while == 2 and es_año_bisiesto(año):
            dia_bisiesto = 1
        mes_while += 1
    return dia_absoluto + dia_bisiesto + dia

def calc_dias(date1, date2):
    # dd/mm/yyyy
    lista1 = date1.split("/")
    lista2 = date2.split("/")
    datos_erroneos = encontrar_datos_erroneos(date1, date2)
    if not datos_erroneos:
        # (día, mes, año)
        fecha1 = tuple([int(dato) for dato in lista1])
        fecha2 = tuple([int(dato) for dato in lista2])
        # Dentro del mismo año, debemos considerar los días de cada mes
        dias_en_cada_mes = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 
            6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
            11: 30, 12: 31 
        }
        # Creamos variables para los días, meses y años
        day1, month1, year1 = fecha1
        day2, month2, year2 = fecha2
        diferencia_años = abs(year2 - year1)
        diferencia_meses = abs(month2 - month1)
    
        # índices del 0 al 11 para los meses !
        dias_mes = list(dias_en_cada_mes.values())

        if diferencia_años == 0:
        
            dia1_absoluto, dia2_absoluto = 0, 0
            if diferencia_meses == 0:
                return abs(day2-day1)
            else:
                mes = 1
                while mes < month1 or mes < month2:
                    if mes < month1:
                        dia1_absoluto += dias_mes[mes-1]
                    if mes < month2:
                        dia2_absoluto += dias_mes[mes-1]
                    mes += 1
                dia1_absoluto += day1
                dia2_absoluto += day2
                return abs(dia2_absoluto - dia1_absoluto)
        else:
        # Entre años, debemos considerar también los bisiestos
            # diferencia = sum(dias_mes)*(diferencia_años)
            # 1. Determinar qué fecha es posterior -> inicio, fin
            # 2. Empezando en inicio, sumamos días hasta fin
            # 3. Tener en cuenta bisiestos
            if year1 > year2:
                dia_ini, mes_ini, año_ini = fecha2 
                dia_fin, mes_fin, año_fin = fecha1
            elif year2 > year1:
                dia_ini, mes_ini, año_ini = fecha1 # ok
                dia_fin, mes_fin, año_fin = fecha2 # ok

            # Replanteamos esta parte con días absolutos por cada año considerado en el bucle
            
            # Este entra en juego cuando hay más de 1 año de por medio
            delta_2 = 0
            dias_bisiestos = 0
            if diferencia_años > 1:
                for año_for in range(año_ini+1, año_fin):
                    if es_año_bisiesto(año_for):
                        dias_bisiestos += 1
                    delta_2 += 365

            # Mínimo hay un cambio de mes
            delta_1 = 0 
            dias_totales_año_ini = 365
            if es_año_bisiesto(año_ini):
                dias_totales_año_ini += 1
            delta_1 = dias_totales_año_ini - calc_dia_absoluto(dia_ini, mes_ini, año_ini, dias_mes) # 31-14 = 17

            delta_3 = calc_dia_absoluto(dia_fin, mes_fin, año_fin, dias_mes) # 10
            return delta_1 + delta_2 + delta_3 + dias_bisiestos
    else:
        raise Exception(f"Los inputs {datos_erroneos} no tienen formato de fecha correcto: dd/mm/aaaa")
main()