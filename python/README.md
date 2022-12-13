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
## .gitignore
Hemos configurado el `.gitignore` para que si permita hacer seguimiento de `requirements.txt`:
```
    # created by virtualenv automatically
    *
    !.gitignore
    !requirements.txt
```