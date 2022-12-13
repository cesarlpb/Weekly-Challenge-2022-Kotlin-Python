# Challenge 0

# /*
#  * Reto #5
#  * ASPECT RATIO DE UNA IMAGEN
#  * Fecha publicación enunciado: 01/02/22
#  * Fecha publicación resolución: 07/02/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
#  * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
#  * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */
#%% 1. Bajar la imagen a partir de la URL -> request y la guardamos en local con shutils
# https://www.scrapingbee.com/blog/download-image-python/
import requests # request img from web
import shutil # save img locally

url = "https://www.freecodecamp.org/news/content/images/size/w2000/2022/02/Banner-10.png"
response = requests.get(url, stream = True)
filename = "img/imagen1.png"
if response.status_code == 200:
    with open(filename,'wb') as f:
        shutil.copyfileobj(response.raw, f)
    print('Hemos guardado la imagen como:',filename)
else:
    print('La img no se pudo descargar :(')
#%% 2. Obtener los datos de la imagen de ancho y alto -> PIL
# https://www.geeksforgeeks.org/how-to-find-width-and-height-of-an-image-using-python/
# Importamos Image de PIL (pillow)
from PIL import Image
  
# nombre del archivo
file_path = "img/imagen1.png"
img = Image.open(file_path)
  
# Ancho y alto de img
width = img.width
height = img.height

print("Ancho:", width, "px")
print("Altura:", height, "px")
#%% 3. Calcular el aspect ratio como el cociente y simplificar a una "fracción simple" -> Fraction
# https://stackoverflow.com/questions/23344185/how-to-convert-a-decimal-number-into-fraction
from fractions import Fraction
aspect_ratio = round(width / height, 15)
fraccion = Fraction(aspect_ratio).limit_denominator()
print("Aspect ratio:", fraccion)
# %%
