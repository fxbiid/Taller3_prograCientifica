from collections import defaultdict
import random


class GeneradorNGramas:

    def __init__(self, n=2):
        self.n = n
        self.modelo = defaultdict(list)

    def entrenar(self, textos):
        for texto in textos:
            palabras = texto.lower().split()
            for i in range(len(palabras) - self.n):
                clave = tuple(palabras[i:i+self.n])
                siguiente = palabras[i+self.n]
                self.modelo[clave].append(siguiente)

    def generar(self, inicio="", longitud=30):

        palabras = inicio.lower().split()

        if self.n == 1:

            if not palabras:
                palabras.append(random.choice(list(self.modelo.keys()))[0])

            while len(palabras) < longitud:

                clave = (palabras[-1],)

                if clave not in self.modelo:
                    break

                palabras.append(random.choice(self.modelo[clave]))

        else:

            while len(palabras) < longitud:

                if len(palabras) < self.n:
                    break

                clave = tuple(palabras[-self.n:])

                if clave not in self.modelo:
                    break

                palabras.append(random.choice(self.modelo[clave]))

        return " ".join(palabras)