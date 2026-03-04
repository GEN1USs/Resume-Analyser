import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

def clean_text(text: str) -> str:
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def extract_tfidf_features(resumes: list[str]):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(resumes)
    return X, vectorizer