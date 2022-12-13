# Challenge 9

#
#    Reto #9
#    CÓDIGO MORSE
#    Fecha publicación enunciado: 02/03/22
#    Fecha publicación resolución: 07/03/22
#    Dificultad: MEDIA
#   
#    Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
#    - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
#    - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
#    - El alfabeto morse soportado será el mostrado en https:es.wikipedia.org/wiki/Código_morse.
#   
#    Información adicional:
#    - Usa el canal de nuestro discord (https:mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#    - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#    - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#    - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#   
#  

#%% Texto a Morse
def main():
    print(texto_a_morse("Hola, mundo!"))
    texto = morse_a_texto(texto_a_morse("Hola, mundo!"))
    print("texto:", texto)
alfanum_morse = {
"A": "· —",         "N": "— ·",         "0": "— — — — —",
"B": "— · · ·",     "Ñ": "— — · — —",   "1": "· — — — —",
"C": "— · — ·",     "O": "— — —",       "2": "· · — — —",
"CH": "— — — —",    "P": "· — — ·",     "3": "· · · — —",
"D": "— · ·",       "Q": "— — · —",	 	"4": "· · · · —",
"E":	"·",        "R": "· — ·",       "5": "· · · · ·",
"F": "· · — ·",     "S": "· · ·",       "6": "— · · · ·",
"G":	"— — ·",    "T": "—",           "7": "— — · · ·",
"H":	"· · · ·",  "U": "· · —",       "8": "— — — · ·",
"I":	"· ·",	 	"V":	"· · · —",	"9": "— — — — ·",
"J":	"· — — —",	"W":	"· — —",	".":	"· — · — · —",
"K":	"— · —",	"X":	"— · · —",	",":	"— — · · — —",
"L":	"· — · ·",	"Y":	"— · — —",	"?":	"· · — — · ·",
"M":	"— —",      "Z":	"— — · ·",	"\"":	"· — · · — ·",	 
"/":	"— · · — ·", "!": ". . . - - - . . . - - -",
"error": "....--.....---..-...-.."
}
def texto_a_morse(string):
    # Usamos dict y chars separados por espacio y palabras por dos espacios
    morse = ""
    string = string.upper()
    for char in string:
        chars_en_morse = alfanum_morse.get(char)
        if chars_en_morse != None:
            morse += chars_en_morse.replace(" ","") + " "
        elif char == " ":
            morse += "  "
    return morse
def morse_a_texto(string):
    # string -> espacio entre chars y doble espacio entre palabras
    values = [value.replace(" ", "") for value in list(alfanum_morse.values())]
    keys = list(alfanum_morse.keys())
    palabras = string.split("  ")
    texto = ""
    for palabra in palabras:
        chars = palabra.split(" ")
        for char in chars: 
            if char in values:
                idx = values.index(char)
                letra = keys[idx]
                texto += letra
        texto += " "
    return texto.capitalize()
main()