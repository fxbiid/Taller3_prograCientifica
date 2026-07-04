from gensim.models import Word2Vec
import numpy as np


class Word2VecModel:

    def __init__(self):
        self.modelo = None

    def entrenar(self,documentos,vector_size=100,window=5,min_count=1,workers=4):

        self.modelo = Word2Vec(sentences=documentos,vector_size=vector_size,window=window,min_count=min_count,workers=workers)

    def obtener_embeddings(self, documentos):
        embeddings = []

        for doc in documentos:
            vectores = []

            for palabra in doc:
                if palabra in self.modelo.wv:
                    vectores.append(self.modelo.wv[palabra])

            if len(vectores) == 0:
                embeddings.append(np.zeros(self.modelo.vector_size))

            else:
                embeddings.append(
                    np.mean(vectores,axis=0))

        return np.array(embeddings)