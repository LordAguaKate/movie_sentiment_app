from flask import Flask, render_template, request
import joblib
import sqlite3
import os

app = Flask(__name__)

# Cargar los modelos en la memoria global de la app
# Es importante manejar excepciones por si olvidas correr train_model.py
try:
    vectorizer = joblib.load('models/vectorizer.pkl')
    model = joblib.load('models/sentiment_model.pkl')
except FileNotFoundError:
    print("Error: No se encontraron los modelos. Corre 'python train_model.py' primero.")
    exit(1)

# Función helper para conectar a la DB
def get_db_connection():
    conn = sqlite3.connect('reviews.sqlite')
    conn.row_factory = sqlite3.Row # Permite acceder a las columnas por nombre
    return conn

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_review = request.form['review']
        
        # 1. Preprocesar (idealmente limpiar el HTML aquí también) y predecir
        import re
        clean_user_review = re.sub(r'<[^>]*>', '', user_review)
        vect_review = vectorizer.transform([clean_user_review])
        
        raw_prediction = model.predict(vect_review)[0]
        prediction = 'positive' if raw_prediction == 1 else 'negative'
        
        # 2. Guardar en SQLite
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO reviews (review_text, sentiment) VALUES (?, ?)',
            (user_review, prediction)
        )
        conn.commit()
        conn.close()
        
        # 3. Renderizar resultados
        return render_template('results.html', review=user_review, prediction=prediction)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    conn = get_db_connection()
    reviews = conn.execute('SELECT * FROM reviews ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('dashboard.html', reviews=reviews)

if __name__ == '__main__':
    # Habilitamos el modo debug para el desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)