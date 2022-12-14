# Challenge 15

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
    # Sin datetime
    print(calc_dias("18/05/2022", "29/05/2022"))    # 11 días
    print(calc_dias("mouredev", "29/04/2022"))      # Error
    print(calc_dias("18/5/2022", "29/04/2022"))     # 19 días
    # Con datetime
    str_d1 = '20/10/2021'
    str_d2 = '20/2/2022'
    print(str_d2, "-", str_d1, ":", calc_dias_datetime(str_d1, str_d2))
    # Test
    print(calc_dias_datetime("18/05/2022", "29/05/2022"))
    # print(calc_dias_datetime("asdf", "29/04/2022"))
    print(calc_dias_datetime("18/5/2022", "29/04/2022"))
def calc_dias_datetime(date1, date2):
    from datetime import datetime
    # Convertimos strings en obj datetime
    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(date2, "%d/%m/%Y")
    # Calculamos diferencia de fechas en timedelta
    delta = d2 - d1
    return f'Han pasado {delta.days} días'
def calc_dias(date1, date2):
    pass
main()

# fun main() {

#     printDaysBetween("18/05/2022", "29/05/2022")
#     printDaysBetween("mouredev", "29/04/2022")
#     printDaysBetween("18/5/2022", "29/04/2022")
# }

# private fun printDaysBetween(firstDate: String, secondDate: String) {
#     try {
#         println(daysBetween(firstDate, secondDate))
#     } catch (e: DaysBetweenError) {
#         println("Error en el formato de alguna fecha")
#     } catch (e: Exception) {
#             println("Error en el parse de alguna fecha")
#     }
# }

# class DaysBetweenError: Exception()

# private fun daysBetween(firstDate: String, secondDate: String): Int {

#     val formatter = SimpleDateFormat("dd/MM/yyyy")
#     val firstParsedDate = formatter.parse(firstDate)
#     val secondParsedDate = formatter.parse(secondDate)

#     val regex = "^([0-9]){2}[/]([0-9]){2}[/]([0-9]){4}$".toRegex()

#     if (firstParsedDate != null
#         && secondParsedDate != null
#         && firstDate.contains(regex)
#         && secondDate.contains(regex)
#     ) {

#         return TimeUnit.DAYS.convert(
#             firstParsedDate.time - secondParsedDate.time,
#             TimeUnit.MILLISECONDS
#         ).toInt().absoluteValue
#     }
#     throw DaysBetweenError()
# }