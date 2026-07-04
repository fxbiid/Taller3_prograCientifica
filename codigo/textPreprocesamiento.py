import re
from collections import Counter

class TextPreprocesamiento:

    def __init__(self):
        self.vocabulary = set()
        self.word_frequencies = Counter()

    def to_lowerCase(self,text):
        return text.lower()

    def remove_puntuacion(self,text):
        return re.sub(r"[^\w\s]", "", text)

    def remove_numbers(self,text):
        return re.sub(r"\d+", "", text)

    def tokenize(self,text):
        return text.split()

    def remove_stopwords(self,tokens):
        stopwords = {
            "the", "a", "an", "and", "of", "to", "in", "for", "is", "on",
            "that", "this", "these", "those",
            "he", "she", "it", "they", "them", "him", "her",
            "his", "hers", "their", "its",
            "i", "me", "my", "mine",
            "we", "our", "ours",
            "you", "your", "yours",
            "who", "whom", "whose", "which", "what",
            "be", "been", "being", "am", "are", "was", "were",
            "do", "does", "did",
            "have", "has", "had",
            "shall", "will", "would", "should", "may", "might",
            "can", "could", "must",
            "not", "no", "nor",
            "if", "then", "than",
            "as", "at", "by", "from", "into", "out", "over", "under",
            "with", "without", "about", "after", "before",
            "there", "here", "where", "when", "why", "how",
            "all", "any", "both", "each", "few", "more", "most", "other",
            "some", "such", "only", "own", "same", "so", "too", "very",
            "thou", "thee", "thy", "thine", "unto", "ye"
        }
        return [
            word
            for word in tokens
            if word not in stopwords and len(word) > 2
        ]

    def preprocess(self, text):

        text = self.to_lowerCase(text)

        text = self.remove_puntuacion(text)

        text = self.remove_numbers(text)

        tokens = self.tokenize(text)

        tokens = self.remove_stopwords(tokens)

        self.vocabulary.update(tokens)

        self.word_frequencies.update(tokens)

        return tokens