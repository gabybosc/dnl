import numpy as np
import string
import collections
from collections import Counter
import matplotlib.pyplot as plt
plt.ion()

# plt.figure()
# for cuentos in ['the_bicentennial_man.txt', 'Aura_Carlos_Fuentes.txt', 'non_approfondire.txt']:
#     palabras = []
#     palabras2 = []
#     with open(cuentos, 'r') as f:
#         n = f.readlines()
#         preliminar = []
#         for _ in n:
#             preliminar.append(_.rstrip('\n').split())
#         palabras_simbolos = []
#         for lista in preliminar:
#             for _ in lista:
#                 palabras_simbolos.append(_.lstrip('—').rstrip('—'))
#         for _ in palabras_simbolos:
#             palabras.append(_.translate(str.maketrans('', '', string.punctuation)))
#         for _ in palabras:
#             palabras2.append(_.lower())
#
#     print(f'El cuento {cuentos} tiene {len(palabras2)} palabras')
#     ranking = Counter(palabras2)
#     ranking_ordenado = [(k) for k,l in sorted([(j,i) for i,j in ranking.items()], reverse=True)]
#
#     lista_palabras = np.array([i+1 for i in range(len(ranking_ordenado))])
#     a,b = np.polyfit(np.log(lista_palabras[15:500]), np.log(ranking_ordenado[15:500]), 1)
#
#     f_lineal = a * np.log(lista_palabras) + b
#     f_exp = np.exp(f_lineal)
#
#     plt.loglog(ranking_ordenado, '.', label=f'{cuentos}')
#     plt.loglog(lista_palabras, f_exp, label=f'Pendiente = {a:g}')
#     plt.title('P(k) para cuentos')
#     plt.xlabel('Palabras')
#     plt.ylabel('Frecuencia')
#     plt.legend()

plt.figure()
for clasicos in ['pride_and_prejudice.txt', 'quijote.txt', 'divina_comedia.txt']:
    palabras = []
    palabras2 = []
    with open(clasicos, 'r') as f:
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

    print(f'El clásico {clasicos} tiene {len(palabras2)} palabras')
    ranking = Counter(palabras2)
    ranking_ordenado = [(k) for k,l in sorted([(j,i) for i,j in ranking.items()], reverse=True)]

    lista_palabras = np.array([i+1 for i in range(len(ranking_ordenado))])
    a,b = np.polyfit(np.log(lista_palabras[15:500]), np.log(ranking_ordenado[15:500]), 1)

    f_lineal = a * np.log(lista_palabras) + b
    f_exp = np.exp(f_lineal)

    plt.loglog(ranking_ordenado, '.', label=f'{clasicos}')
    plt.loglog(lista_palabras, f_exp, label=f'Pendiente = {a:g}')
    plt.title('P(k) para clasicos')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.legend()

# plt.figure()
# for palabras_aleatorias in ['random1.txt', 'random2.txt', 'random3.txt']:
#     palabras = []
#     palabras2 = []
#     with open(palabras_aleatorias, 'r') as f:
#         n = f.readlines()
#         preliminar = []
#         for _ in n:
#             preliminar.append(_.rstrip('\n').split())
#         palabras_simbolos = []
#         for lista in preliminar:
#             for _ in lista:
#                 palabras_simbolos.append(_.lstrip('—').rstrip('—'))
#         for _ in palabras_simbolos:
#             palabras.append(_.translate(str.maketrans('', '', string.punctuation)))
#         for _ in palabras:
#             palabras2.append(_.lower())
#
#     print(f'El texto {palabras_aleatorias} tiene {len(palabras2)} palabras')
#     ranking = Counter(palabras2)
#     ranking_ordenado = [(k) for k,l in sorted([(j,i) for i,j in ranking.items()], reverse=True)]
#
#     plt.plot(ranking_ordenado, '.', label=f'{palabras_aleatorias}')
#     plt.title('P(k) para textos sin comunicación')
#     plt.xlabel('Palabras')
#     plt.ylabel('Frecuencia')
#     plt.legend()
