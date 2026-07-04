import pandas as pd
class BibliaDataset:

        def __init__(self, verses_path, books_path):
            self.verses_path = verses_path
            self.books_path = books_path
            self.data = None

        def load_data(self):
            verses = pd.read_csv(self.verses_path)
            books = pd.read_csv(self.books_path)

            self.data = verses.merge(
                books,
                on="b"
            )

            return self.data