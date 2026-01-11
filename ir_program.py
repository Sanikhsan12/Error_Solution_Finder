import pandas as pd
import os
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sentence_transformers import SentenceTransformer

# ! Setup NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

class IREngine:
    def __init__(self, metadata_path):
        self.df = pd.read_csv(metadata_path)
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        self.inverted_index = {}
        self.embeddings = None
        # ! Model SBERT
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    # ! Preprocessing: Tokenization, Stemming, Stopword Removal
    def preprocess(self, text):
        if not isinstance(text, str): return []
        # ? Tokenisasi
        tokens = nltk.word_tokenize(text.lower())
        # ? Stemming & Stopword Removal
        cleaned = [self.stemmer.stem(w) for w in tokens if w.isalnum() and w not in self.stop_words]
        return cleaned

    # ! Inverted Index Building
    def build_inverted_index(self):
        print("Membangun Inverted Index")
        for idx, row in self.df.iterrows():
            if os.path.exists(row['text_path']):
                with open(row['text_path'], 'r', encoding='utf-8') as f:
                    tokens = self.preprocess(f.read())
                    for token in set(tokens):
                        if token not in self.inverted_index:
                            self.inverted_index[token] = []
                        self.inverted_index[token].append(row['doc_id'])
        print(f"Index selesai: {len(self.inverted_index)} term unik tersimpan.")

    # ! Menghitung Cosine Similarity Manual
    def get_cosine_similarity(self, v1, v2):
        dot_product = np.dot(v1, v2)
        norm_v1 = np.linalg.norm(v1)
        norm_v2 = np.linalg.norm(v2)
        return dot_product / (norm_v1 * norm_v2) if (norm_v1 * norm_v2) > 0 else 0

    # ! Vector Space Model Search
    def prepare_search(self):
        print("Menyiapkan vektor dokumen...")
        all_texts = []
        for path in self.df['text_path']:
            with open(path, 'r', encoding='utf-8') as f:
                all_texts.append(f.read())
        self.embeddings = self.model.encode(all_texts)

    # ! Search Function
    def search(self, query, top_n=3):
        query_vec = self.model.encode([query])[0]
        scores = []
        for i, doc_vec in enumerate(self.embeddings):
            sim = self.get_cosine_similarity(query_vec, doc_vec)
            scores.append((i, sim))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_n]

    # ! Generate Summary
    def generate_summary(self, doc_id):
        path = self.df.iloc[doc_id]['text_path']
        with open(path, 'r', encoding='utf-8') as f:
            sentences = nltk.sent_tokenize(f.read())
            # ! Simple summary: first 2 sentences
            return " ".join(sentences[:2]) + "..."