import pytest 

def es_palindromo(string):
    string_sin_caracteres_especiales = ""
    for char in string:
        if char.isalnum():
            string_sin_caracteres_especiales += char.lower()
    return string_sin_caracteres_especiales == string_sin_caracteres_especiales[::-1]
# True
"""
Ana lleva al oso la avellana.
Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida
Ana
"""
# False
"""
¿Qué os ha parecido el reto?
asdf
102
"""
def test_es_palindromo_debe_devolver_true():
    pass
def test_es_palindromo_debe_devolver_false():
    pass

pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?",
])
# Terminar ejercicio de parametrizar tests