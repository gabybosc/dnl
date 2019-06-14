import numpy as np
import random

"""
abre un archivo con 720000 palabras en inglés. Luego, crea una string con 15000 palabras seleccionadas de manera aleatoria. Finalmente lo guarda en un archivo nuevo.
"""

with open('words.txt', 'r') as f:
    n = f.readlines()
    string = []
    for i in range(15000):
        numero_random = random.randint(0, len(n))
        string.append(n[numero_random].rstrip('\n'))

with open("random3.txt", "w") as o:
    for line in string:
        print("{}".format(line), file=o)
