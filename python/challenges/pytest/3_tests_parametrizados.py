import pytest 

def es_palindromo(string):
    from unidecode import unidecode
    string_sin_caracteres_especiales = ""
    for char in string:
        if char.isalnum():
            string_sin_caracteres_especiales += char.lower()
            string_sin_caracteres_especiales = unidecode(string_sin_caracteres_especiales.replace(" ", ""))
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
# Casos que devuelven True
def test_es_palindromo_debe_devolver_true_1():
    assert es_palindromo("Ana lleva al oso la avellana.") == True
    assert es_palindromo("Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida.") == True
    assert es_palindromo("Ana") == True
def test_es_palindromo_debe_devolver_true_con_lista_1():
    lista_de_inputs_que_devuelve_true = ["Ana lleva al oso la avellana.", "Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida.", "Ana"]
    for i in range(len(lista_de_inputs_que_devuelve_true)):
        assert es_palindromo(lista_de_inputs_que_devuelve_true[i]) == True
# Casos que devuelven False
def test_es_palindromo_debe_devolver_false_1():
    assert es_palindromo("¿Qué os ha parecido el reto?") == False
    assert es_palindromo("asdf") == False
    assert es_palindromo("102") == False
def test_es_palindromo_debe_devolver_false_con_lista_1():
    lista_de_inputs_que_devuelve_false = ["¿Qué os ha parecido el reto?", "asdf", "102", "asdf102", "102asdf"]
    for i in range(len(lista_de_inputs_que_devuelve_false)):
        assert es_palindromo(lista_de_inputs_que_devuelve_false[i]) == False
def test_es_palindromo_debe_devolver_true():
    pass
def test_es_palindromo_debe_devolver_false():
    pass

# pytest.mark.parametrize("palindrome", [
#     "",
#     "a",
#     "Bob",
#     "Never odd or even",
#     "Do geese see God?",
# ])
def main():
    print(es_palindromo("Ana lleva al oso la avellana."))
    print(es_palindromo("Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida."))
    print(es_palindromo("Ana"))

# main()