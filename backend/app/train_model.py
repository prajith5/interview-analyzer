from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample dataset (you can expand later)
texts = [
    "I have experience in python and sql",
    "I built machine learning models",
    "I am not sure about this",
    "maybe I think I can do it",
    "I developed APIs using fastapi",
    "I don't know much about this"
]

# Labels (1 = good answer, 0 = weak answer)
labels = [1, 1, 0, 0, 1, 0]

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Model
model = LogisticRegression()
model.fit(X, labels)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved!")