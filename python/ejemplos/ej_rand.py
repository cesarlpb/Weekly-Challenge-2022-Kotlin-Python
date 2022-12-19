#%% random
import random

print(round(random.random()*100))

#%% otra forma de generar numeros aleatorios
import datetime as dt

print(round(dt.datetime.now().microsecond/1000_000 * 100))

print(round(dt.datetime.now().second/60 * 100))