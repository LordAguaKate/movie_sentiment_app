import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

print("Cargando dataset movie_data.csv...")
df = pd.read_csv('movie_data.csv')

# 1. Preprocesamiento: Limpieza de HTML
print("Limpiando ruido y etiquetas HTML...")
def clean_text(text):
    # Remueve cualquier etiqueta HTML como <br />
    text = re.sub(r'<[^>]*>', '', text)
    return text

df['review_clean'] = df['review'].apply(clean_text)

# 2. Vectorización TF-IDF
print("Vectorizando texto (esto tomará unos segundos)...")
# Subimos a 10,000 features para aprovechar que tenemos más datos
vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
X = vectorizer.fit_transform(df['review_clean'])
y = df['sentiment'] # Recuerda: 1 es Positivo, 0 es Negativo

# 3. Entrenamiento del Modelo
print("Entrenando modelo de Regresión Logística...")
model = LogisticRegression(max_iter=500) # Aumentamos iteraciones por si tarda en converger
model.fit(X, y)

# 4. Exportar artefactos
os.makedirs('models', exist_ok=True)
joblib.dump(vectorizer, 'models/vectorizer.pkl')
joblib.dump(model, 'models/sentiment_model.pkl')

print("¡Modelo entrenado y listo para producción!")