import sqlite3
import os

def get_connection():
    # Ensure 'data' folder exists
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Connect to the SQLite database
    conn = sqlite3.connect("data/hostel.db")
    return conn

def setup_database():
    conn = get_connection()
    c = conn.cursor()

    # Create students table
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll_no TEXT UNIQUE,
            department TEXT
        )
    ''')

    # Create rooms table
    c.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            room_no INTEGER PRIMARY KEY,
            capacity INTEGER,
            available INTEGER
        )
    ''')

    # Create bookings table
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            room_no INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(room_no) REFERENCES rooms(room_no)
        )
    ''')

    conn.commit()
    conn.close()
