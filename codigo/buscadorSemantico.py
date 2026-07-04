from codigo.similitudDelCoseno import SimilitudDelCoseno


class BuscadorSemantico:

    def buscar(self, consulta, matriz_tfidf, vectorizer, preprocessor, df, k=5):
        tokens = preprocessor.preprocess(consulta)

        # Validar si los tokens existen en el vocabulario de vectorizer
        palabras_validas = [t for t in tokens if t in vectorizer.vocabulario]

        if not palabras_validas:
            print("La consulta no contiene términos presentes en el vocabulario.")
            return []

        vector_consulta = vectorizer.transformar_consulta(tokens)

        # Validación extra: si el vector resultante es puro cero
        if all(val == 0 for val in vector_consulta.values()):
            print("La consulta no genera un vector útil (palabras fuera de vocabulario).")
            return []


        similitudes = []

        for i, vector in enumerate(matriz_tfidf):
            sim = SimilitudDelCoseno.calcular(vector_consulta, vector)
            # 2. Exclusión de similitudes 0
            if sim > 0:
                similitudes.append((i, sim))

        similitudes.sort(key=lambda x: x[1], reverse=True)
        return similitudes[:k]