#%% Tests de Challenge18
# Llamamos al main de Challenge18
# Necesitamos indicarle la ruta cuando está en otra carpeta
import sys
sys.path.insert(0, '<ruta absoluta a carpeta de retos>/challenges')
import Challenge18 as challenge # Importar en la misma carpeta
# from Challenge18 import TresEnRaya # Importamos solo la fn TresEnRaya
def main():
    challenge.main()
main()