# Funciones del reto 15

# Marta
import re
# calcula si el año es bisiesto
def isLeapYear(year):
   return not year % 4 and (year % 100 or not year % 400)
 
#Calcula tantos años como pasados por numYears (se pasa el año para saber si
# es bisiesto o no)
def calculateDaysForYear(year, numYears):
   countDays = 0
   for numYear in range(numYears):
       if isLeapYear(year+numYear+1): countDays += 1
       countDays += 365
   return countDays
 
#Devuelve los el número de días que tiene un mes, le pasamos el año para el
# caso de febrero.
def daysByMonth(month, year):
   if month in [1, 3, 4, 5, 8, 10, 12]: return 31   
   elif month in [6, 7, 9, 11]: return 30
   elif month == 2:
       if isLeapYear(year): return 29
       else: return 28

# Calculamos el número de días que hay desde el 1 de enero hasta un mes menos
# al pasado por párametro
def calculateDaysForMonth(month, year):
   return sum([daysByMonth(mon, year) for mon in range(1, month)])

def printDaysBetween(date1, date2):
    regex = re.compile('[0-9]{2}/[0-9]{2}/[0-9]{4}', re.I)
    if bool(regex.match(date1)) and bool(regex.match(date2)):
       date1_s = date1.split("/")
       date2_s = date2.split("/")
       day1, month1, year1 = int(date1_s[0]), int(date1_s[1]), int(date1_s[2])
       day2, month2, year2 = int(date2_s[0]), int(date2_s[1]), int(date2_s[2])
 
       diffDays = abs(day1 - day2)
       diffMonth = abs(month1 - month2)
       diffYear = year1 - year2
       if diffYear == 0:
           if diffMonth == 0:
               totalDays = diffDays
           else:
               totalDays1 = day1 + calculateDaysForMonth(month1, year1)
               totalDays2 = day2 + calculateDaysForMonth(month2, year2)
               totalDays = abs(totalDays1 - totalDays2)
       else:
            totalDays1 = day1 + calculateDaysForMonth(month1, year1)
            totalDays2 = day2 + calculateDaysForMonth(month2, year2)
            # si diffYear > 0 significa que el año de la fecha 1 es más grande
            # que el año de la fecha 2. Por tanto, sumará 365 o 366 x tantos años
            # como haya de diferencia. Si es inferior, lo hará con la fecha 2.
            if diffYear > 0: totalDays1 += calculateDaysForYear(year2, diffYear)
            else: totalDays2 += calculateDaysForYear(year1, -diffYear)
            totalDays = abs(totalDays1 - totalDays2)
       print(f"{totalDays} días de diferencia entre {date1} y {date2}")
       #return totalDays
    else:
       print("El formato introducido es diferente a dd/MM/yyyy")

# Pep
def bisiesto(year):
    if not year % 4:
        if year % 100:
            return True
        elif not year % 100 and not year % 400:
            return True
    return False

dias_en_cada_mes = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 
    6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
    11: 30, 12: 31 
    }
dias_mes = list(dias_en_cada_mes.values())

def dia_absoluto(day, month, year, dias_mes):
    if bisiesto(year):
        dias_mes[1] = 29
    else:
        dias_mes[1] = 28
    dia_absoluto = 0
    dia, mes = 1,1
    while mes <= month and dia <= dia:
        if mes < month:
            dia_absoluto += dias_mes[mes-1]
        mes += 1
    dia_absoluto += day
    return dia_absoluto