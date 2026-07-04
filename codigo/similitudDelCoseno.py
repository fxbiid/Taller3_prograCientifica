from math import sqrt


class SimilitudDelCoseno:

    @staticmethod
    def calcular(vector1, vector2):
        # 1. Si los vectores son diccionarios (formato disperso optimizado)
        if isinstance(vector1, dict) and isinstance(vector2, dict):
            claves_comunes = set(vector1.keys()) & set(vector2.keys())

            producto_punto = sum(vector1[k] * vector2[k] for k in claves_comunes)
            norma1 = sqrt(sum(v * v for v in vector1.values()))
            norma2 = sqrt(sum(v * v for v in vector2.values()))

        # 2. Si los vectores son listas o arrays (formato denso clásico)
        else:
            producto_punto = sum(a * b for a, b in zip(vector1, vector2))
            norma1 = sqrt(sum(a * a for a in vector1))
            norma2 = sqrt(sum(b * b for b in vector2))

        # Evitar división por cero
        if norma1 == 0 or norma2 == 0:
            return 0

        return producto_punto / (norma1 * norma2)
