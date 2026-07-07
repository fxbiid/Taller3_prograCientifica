from codigo.bibliaDataset import BibliaDataset
from codigo.textPreprocesamiento import TextPreprocesamiento
from codigo.tfIdf import TfIdf
from codigo.buscadorSemantico import BuscadorSemantico
from codigo.visualizacionPca import VisualizacionPca
from codigo.word2vec import Word2VecModel
from codigo.generadorNGramas import GeneradorNGramas

class Cache:

    def __init__(self):

        biblia = BibliaDataset(
            "data/t_kjv.csv",
            "data/key_english.csv"
        )

        self.df = biblia.load_data()

        self.preprocessor = TextPreprocesamiento()

        documentos = []

        for texto in self.df["t_x"]:
            documentos.append(
                self.preprocessor.preprocess(str(texto))
            )

        self.vectorizer = TfIdf()

        self.vectorizer.fit(documentos)

        self.matriz_tfidf = self.vectorizer.transform(documentos)
        # Convertimos la matriz dispersa a una matriz numérica
        matriz = []

        for vector in self.matriz_tfidf:

            fila = [0.0] * len(self.vectorizer.vocabulario)

            for indice, valor in vector.items():
                fila[indice] = valor

            matriz.append(fila)

        self.visualizador = VisualizacionPca()

        self.pca2d, self.varianza2d = self.visualizador.reducir_dimensiones(
            matriz,
            componentes=2
        )

        self.pca3d, self.varianza3d = self.visualizador.reducir_dimensiones(
            matriz,
            componentes=3
        )
        self.word2vec = Word2VecModel()

        self.word2vec.entrenar(documentos)

        embeddings = self.word2vec.obtener_embeddings(documentos)

        self.word2vec_pca2d, self.word2vec_varianza2d = (
            self.visualizador.reducir_dimensiones(
                embeddings,
                componentes=2
            )
        )

        self.word2vec_pca3d, self.word2vec_varianza3d = (
            self.visualizador.reducir_dimensiones(
                embeddings,
                componentes=3
            )
        )

        self.buscador = BuscadorSemantico()
        self.generadores = {}

        for n in [1, 2, 3]:
            generador = GeneradorNGramas(n)
            generador.entrenar(self.df["t_x"])
            self.generadores[n] = generador


cache = Cache()