# Movie Sentiment App

Aplicación web de análisis de sentimiento para reseñas de películas.

La app usa Flask para servir la interfaz, un modelo de regresión logística entrenado con `movie_data.csv`, y almacena cada predicción en SQLite para poder ver un historial.

## Características

- Interfaz web simple para enviar reseñas de películas.
- Procesamiento de texto y predicción de sentimiento (positivo/negativo) con un modelo entrenado.
- Historial de predicciones guardado en `reviews.sqlite`.
- Dashboard web para revisar todas las reseñas procesadas.

## Estructura del proyecto

- `app.py` - servidor Flask y rutas web.
- `train_model.py` - carga el dataset, limpia texto, entrena el vectorizador y el modelo, y guarda los archivos en `models/`.
- `database.py` - script para inicializar la base de datos SQLite.
- `movie_data.csv` - dataset de reseñas utilizado para entrenar el modelo.
- `models/` - contenedor de los artefactos entrenados (`vectorizer.pkl` y `sentiment_model.pkl`).
- `templates/` - vistas HTML de la aplicación (`index.html`, `results.html`, `dashboard.html`).
- `static/style.css` - estilos de la interfaz.

## Requisitos

- Python 3.8 o superior.
- Flask
- pandas
- scikit-learn
- joblib

> SQLite no requiere instalación adicional en la mayoría de entornos Python, ya que `sqlite3` es parte de la librería estándar.

## Instalación

1. Clonar el repositorio o copiar el proyecto.
2. Crear y activar un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install flask pandas scikit-learn joblib
```

## Preparar el proyecto

1. Inicializar la base de datos:

```bash
python database.py
```

2. Entrenar el modelo y generar los artefactos:

```bash
python train_model.py
```

Esto creará el directorio `models/` con:

- `vectorizer.pkl`
- `sentiment_model.pkl`

## Ejecutar la aplicación

```bash
python app.py
```

La aplicación se ejecutará en `http://0.0.0.0:5000`.

## Uso

1. Abre la página principal.
2. Ingresa una reseña de película en el formulario.
3. Presiona `Analizar Sentimiento`.
4. Revisa el resultado en la página de resultados.
5. Haz clic en `Ver historial de análisis` para consultar el dashboard con todas las predicciones guardadas.

## Notas importantes

- El modelo está diseñado para reseñas en inglés, ya que el dataset original `movie_data.csv` es de reseñas en inglés.
- El texto se limpia de etiquetas HTML antes de pasar al vectorizador.
- Cada evaluación se guarda en `reviews.sqlite`, junto con el timestamp.

## Licencia

Este repositorio incluye una licencia en el archivo `LICENSE`.
