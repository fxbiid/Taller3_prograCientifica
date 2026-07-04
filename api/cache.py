from codigo.bibliaDataset import BibliaDataset
from codigo.textPreprocesamiento import TextPreprocesamiento
from codigo.tfIdf import TfIdf
from codigo.buscadorSemantico import BuscadorSemantico


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

        self.buscador = BuscadorSemantico()


cache = Cache()