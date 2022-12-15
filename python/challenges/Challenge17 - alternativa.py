# Challenge 17 - alternativa
# Anton
#%% Carrera de obstáculos
pista1='_|_|_|_'
pista2='_|_||_|'
pista3 = '|||||'
pista4= '_|_|_|_'
carrera = ['run','jump','run', 'jump','run', 'jump', 'run']

def main(pista, carrera):
    check_pista=""
    if len(pista) != len(carrera):
        print('La carrera y la pista no cuadran')
        return False
    else:
        for i in range(0,len(pista)):
            if pista[i] == '_' and  carrera[i] == 'run':
                check_pista +='_'
            elif pista[i] == '|' and  carrera[i] == 'jump':
                check_pista +='|'
            elif pista[i] == '|' and  carrera[i] == 'run':
                check_pista +='/'
            elif pista[i] == '_' and  carrera[i] == 'jump':
                check_pista +='x'
    if check_pista == pista:
        return True, check_pista, pista
    else:
        return False, check_pista, pista


main(pista1,carrera)
