#%% Usamos datetime para medir el tiempo de ejecución de un bucle
from datetime import datetime

t1 = datetime.now()
print(t1)
n = 1_000_000
suma = 0
for i in range(1, n+1):
    suma += i
t2 = datetime.now()
print(f"{n}:", t2-t1)