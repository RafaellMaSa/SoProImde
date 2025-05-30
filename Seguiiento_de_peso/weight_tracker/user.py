import sqlite3

DB_NAME = 'weight_tracker.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                  CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER,
                   gender TEXT,
                   height REAL,
                   initial_weight REAL
                )
            ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS measurements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                date TEXT,
                weight REAL,
                waist REAL,
                notes TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
                 )
             ''')
    

def add_user(name, age, gender, height,weight):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                   INSERT INTO users(name, age, gender,height, initial_weight)
                   VALUES (?, ?, ?, ?, ?)
                   ''', (name, age, gender, height, weight))
    

def get_users():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, gender, height, initial_weight From users")
        return cursor.fetchall()

def add_measurement(user_id, date, weight, waist, notes):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                        INSERT INTO measurements(user_id, date, weight, waist, notes)
                        VALUES (?, ?, ?, ?, ?) 
                    ''', (user_id, date, weight, waist, notes))
       

def get_measurements(user_id):
    with sqlite3.connect(DB_NAME) as conn:

        cursor = conn.cursor()
        cursor.execute('''
                    SELECT date, weight, waist, notes FROM measurements
                    WHERE user_id = ? 
                    ORDER BY date DESC
                    ''', (user_id,))
        
        return cursor.fetchall()