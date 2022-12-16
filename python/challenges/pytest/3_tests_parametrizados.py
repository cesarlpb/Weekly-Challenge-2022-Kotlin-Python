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
# Tests parametrizado
@pytest.mark.parametrize("palindromo", [
    "Ana lleva al oso la avellana.",
    "Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida.",
    "Ana",
    "101"
])
def test_es_palindromo_debe_devolver_true_parametrizado(palindromo):
    assert es_palindromo(palindromo)
    
# Casos que devuelven False
def test_es_palindromo_debe_devolver_false_1():
    assert es_palindromo("¿Qué os ha parecido el reto?") == False
    assert es_palindromo("asdf") == False
    assert es_palindromo("102") == False
def test_es_palindromo_debe_devolver_false_con_lista_1():
    lista_de_inputs_que_devuelve_false = ["¿Qué os ha parecido el reto?", "asdf", "102", "asdf102", "102asdf"]
    for i in range(len(lista_de_inputs_que_devuelve_false)):
        assert es_palindromo(lista_de_inputs_que_devuelve_false[i]) == False
# Tests parametrizados
@pytest.mark.parametrize("palindromo", [
    "¿Qué os ha parecido el reto?",
    "asdf",
    "102",
    "asdf102",
])
def test_es_palindromo_debe_devolver_false_parametrizado(palindromo):
    assert not es_palindromo(palindromo)

# Parametrizamos ambos casos -> True y False

@pytest.mark.parametrize("posible_palindromo, resultado_esperado", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
    ("palindrome", False),
    ("nope", False),
    ("asadadadadad", False),
])
def test_es_palindromo_debe_devolver_true_o_false(posible_palindromo, resultado_esperado):
    assert es_palindromo(posible_palindromo) == resultado_esperado

def main():
    print(es_palindromo("Ana lleva al oso la avellana."))
    print(es_palindromo("Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida."))
    print(es_palindromo("Ana"))

# main()