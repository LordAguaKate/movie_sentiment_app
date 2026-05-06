import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

print("Cargando dataset movie_data.csv...")
df = pd.read_csv('movie_data.csv')

print("Limpiando ruido y etiquetas HTML...")
def clean_text(text):
    text = re.sub(r'<[^>]*>', '', text)
    return text

df['review_clean'] = df['review'].apply(clean_text)

print("Vectorizando texto (esto tomará unos segundos)...")
vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
X = vectorizer.fit_transform(df['review_clean'])
y = df['sentiment'] 

print("Entrenando modelo de Regresión Logística...")
model = LogisticRegression(max_iter=500) 
model.fit(X, y)

os.makedirs('models', exist_ok=True)
joblib.dump(vectorizer, 'models/vectorizer.pkl')
joblib.dump(model, 'models/sentiment_model.pkl')

print("¡Modelo entrenado y listo para producción!")