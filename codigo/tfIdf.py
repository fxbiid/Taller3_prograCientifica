from math import log
from collections import Counter

class TfIdf:

    def __init__(self):
        self.vocabulario = {}
        self.idf = {}

    #construccion de vocabulario
    def fit(self, documentos):

        vocab = set()

        for doc in documentos:
            vocab.update(doc)

        self.vocabulario = {
            word: idx
            for idx, word in enumerate(sorted(vocab))
        }

        total_docs = len(documentos)

        for word in self.vocabulario:
            docs_with_word = sum(
                1 for doc in documentos
                if word in doc
            )

            self.idf[word] = log(
                total_docs / (1 + docs_with_word)
            )

        # Tf-IDF con Representación Dispersa (Diccionarios)
    def transform(self, documentos):
        matrix = []
        for docu in documentos:
            tf = Counter(docu)
            vector_disperso = {}  # Usamos diccionario en vez de lista

            # Solo iteramos sobre las palabras que ESTÁN en el documento
            for word, tf_value in tf.items():
                if word in self.vocabulario:
                    idx = self.vocabulario[word]
                    tfidf = tf_value * self.idf.get(word, 0)
                    vector_disperso[idx] = tfidf

            matrix.append(vector_disperso)
        return matrix


    def transformar_consulta(self, tokens):
        tf = Counter(tokens)
        vector_disperso = {}

        for palabra, tf_value in tf.items():
            if palabra in self.vocabulario:
                idx = self.vocabulario[palabra]
                idf = self.idf.get(palabra, 0)
                vector_disperso[idx] = tf_value * idf

        return vector_disperso
