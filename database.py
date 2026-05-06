import sqlite3

def init_db():
    conn = sqlite3.connect('reviews.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review_text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Base de datos 'reviews.sqlite' inicializada correctamente.")

if __name__ == '__main__':
    init_db()