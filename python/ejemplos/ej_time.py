#%% Medimos tiempo con time.time()
import time
init = time.time()
n = 1_000_000
suma = 0
for i in range(1, n+1):
    suma += i
fin = time.time()
print(f'{fin-init} segundos en ejecutarse')