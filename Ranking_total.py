import numpy as np
import string
import collections
from collections import Counter
import matplotlib.pyplot as plt
plt.ion()

palabras = []
palabras2 = []
for english in ['Pride_and_prejudice.txt', 'A_tale_of_two_cities.txt', 'Alice_in_wonderland.txt', 'Dracula.txt', 'Frankenstein.txt', 'Moby_Dick.txt', 'Sherlock_Holmes.txt', 'The_importance_of_being_earnest.txt', 'Tom_Sawyer.txt', 'Ulysses.txt']:
    with open(english, 'r') as f:
        n = f.readlines()
        preliminar = []
        for _ in n:
            preliminar.append(_.rstrip('\n').split())
        palabras_simbolos = []
        for lista in preliminar:
            for _ in lista:
                palabras_simbolos.append(_.lstrip('—').rstrip('—'))
        for _ in palabras_simbolos:
            palabras.append(_.translate(str.maketrans('', '', string.punctuation)))
        for _ in palabras:
            palabras2.append(_.lower())
        print(english)

ranking = Counter(palabras2)
ranking_ordenado = np.array([(k) for k,l in sorted([(j,i) for i,j in ranking.items()], reverse=True)])
ranking_normalizado = ranking_ordenado/np.linalg.norm(ranking_ordenado)
ranking_ordenado_con_palabras = [(k, l) for k,l in sorted([(j,i) for i,j in ranking.items()], reverse=True)]
with open(f'ranking_ingles.csv', 'w') as fp:
    fp.write('\n'.join('{},{}'.format(x[0],x[1]) for x in ranking_ordenado_con_palabras[0:10]))


lista_palabras = np.array([i+1 for i in range(len(ranking_normalizado))])
a,b = np.polyfit(np.log(lista_palabras[15:1500]), np.log(ranking_normalizado[15:1500]), 1)

f_lineal = a * np.log(lista_palabras) + b
f_exp = np.exp(f_lineal)
titulo = english.rstrip('.txt').replace('_', ' ')

plt.loglog(ranking_normalizado, '.')
plt.loglog(lista_palabras, f_exp, label=f'Pendiente = {a:g}')
plt.title('P(k) para diez libros en inglés')
plt.xlabel('Palabras')
plt.ylabel('Frecuencia')
plt.legend()



palabras = []
palabras2 = []
for espanol in ['Aura_Carlos_Fuentes.txt', 'Don_Quijote.txt', 'La_cautiva.txt', 'La_vida_es_sueno.txt', 'Rayuela.txt', 'El_buscon.txt', 'Cantar_de_mio_Cid.txt', 'Don_Juan_Tenorio.txt', 'Lazarillo_de_Tormes.txt', 'Martin_Fierro.txt']:
    with open(espanol, 'r') as f:
        n = f.readlines()
        preliminar = []
        for _ in n:
            preliminar.append(_.rstrip('\n').split())
        palabras_simbolos = []
        for lista in preliminar:
            for _ in lista:
                palabras_simbolos.append(_.lstrip('—').rstrip('—'))
        for _ in palabras_simbolos:
            palabras.append(_.translate(str.maketrans('', '', string.punctuation)))
        for _ in palabras:
            palabras2.append(_.lower())
        print(espanol)

ranking = Counter(palabras2)
ranking_ordenado = np.array([k for k,l in sorted([(j,i) for i,j in ranking.items()], reverse=True)])
ranking_normalizado = ranking_ordenado/np.linalg.norm(ranking_ordenado)
ranking_ordenado_con_palabras = [(k, l) for k,l in sorted([(j,i) for i,j in ranking.items()], reverse=True)]

with open(f'ranking_espanol.csv', 'w') as fp:
    fp.write('\n'.join('{},{}'.format(x[0],x[1]) for x in ranking_ordenado_con_palabras[0:10]))

lista_palabras = np.array([i+1 for i in range(len(ranking_normalizado))])
a,b = np.polyfit(np.log(lista_palabras[15:1500]), np.log(ranking_normalizado[15:1500]), 1)

f_lineal = a * np.log(lista_palabras) + b
f_exp = np.exp(f_lineal)
titulo = espanol.rstrip('.txt').replace('_', ' ')

plt.figure()
plt.loglog(ranking_normalizado, '.')
plt.loglog(lista_palabras, f_exp, label=f'Pendiente = {a:g}')
plt.title('P(k) para diez libros en español')
plt.xlabel('Palabras')
plt.ylabel('Frecuencia')
plt.legend()
