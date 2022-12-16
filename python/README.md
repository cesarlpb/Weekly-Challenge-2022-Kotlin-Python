# Notas sobre entornos virtuales e instalaciones

## Instalación del entorno virtual
Comprobamos versión con:
```
virtualenv --version
```
Instalamos `virtualenv` con:
```
pip install virtualenv
```
Creamos entorno virtual con:
```
virtualenv -p python3 nombre_del_entorno
```
o
```
python3 -m venv nombre_del_entorno
```
Más info: [virtualenv](https://learnpython.com/blog/how-to-use-virtualenv-python/)

- Si no funciona bien el entorno virtual o hay problemas a la hora de instalar en el global, intérprete online:

[Online Python](https://www.online-python.com/)

### Activar venv y desactivar
- Activamos el entorno virtual antes de instalar
```
source bin/activate
```
o
```
. ./bin/activate
```
Desactivar con:
```
deactivate
```
## Requests
Primero, miramos si lo tenemos instalado:
```
python -m pip show requests
```
Si no lo tenemos, instalamos con:
```
pip install requests
```
Ahora sí, `show` debe arrojar información.

- [Instalación de requests](https://www.activestate.com/resources/quick-reads/how-to-pip-install-requests-python-package/)

## Shutils 
```
pip install shutils
```
## pillow & PIL

```
pip install pillow
```
Para ver la lista de paquetes instalados:
```
python3 -m pip list
```
- [Fuente](https://stackoverflow.com/questions/68439152/how-to-install-pil-with-pip)

## Fraction
```
pip install Fraction
```

Para escribir en `requirements.txt` los paquetes instalados en el `venv` usamos:
```
pip freeze > requirements.txt
```
Para instalar todos los paquetes de nnuevo:
```
pip install -r "ruta_a_requirements.txt"
```
## Unidecode

```
pip install Unidecode
```
- [Más información](https://pypi.org/project/Unidecode/)

## Datetime
```
pip install datetime
```
[Ejemplo de uso](https://pynative.com/python-difference-between-two-dates/)

## Enums
```
pip install enum
```
* **Nota: instalar en entorno virtual porque puede dar problemas en global**
[Documentación oficial](https://pypi.org/project/enum/)

# Testing con PyTest
```
pip install pytest
```
## Ejecución de tests
- Ejecución de tests de un archivo:
```
pytest nombre_archivo_test.py
```
- Formato de salida más detallado:
```
pytest -v nombre_archivo_test.py
```
```
pytest -v -s nombre_archivo_test.py
```
- Formato de salida más resumido:
```
pytest -q nombre_archivo_test.py
```
### Más formas de ejecutar tests
- Ejecución de tests que contienen substring (en nombre):
```
pytest nombre_de_archivo -k substring
```
- Añadiendo `-v` o `-q` para más o menos detalle: 
```
pytest nombre_de_archivo -k substring -v
```
[Ejemplos más personalizados de ejecución de tests](https://programmerclick.com/article/1422390515/)
[Ejemplos oficiales](https://docs.pytest.org/en/7.1.x/getting-started.html)
[Más información](https://pypi.org/project/pytest/)
## Generación de Reportes con Pytest-html
```
pip install pytest-html
```
```
pytest nombre_archivo_test.py --html=nombre_archivo_reporte.html
```

```
import pytest
from py.xml import html

def pytest_html_report_title(report)
   report.title = "My very own title!"
```
- [Respuesta en Stackoverflow](https://stackoverflow.com/questions/29123840/how-to-generate-test-report-using-pytest)
- [pytest-html](https://pypi.org/project/pytest-html/)

## .gitignore
Hemos configurado el `.gitignore` para que si permita hacer seguimiento de `requirements.txt`:
```
    # created by virtualenv automatically
    *
    !.gitignore
    !requirements.txt
```