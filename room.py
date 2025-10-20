from database import get_connection

def add_room(room_no, capacity):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO rooms (room_no, capacity, available) VALUES (?, ?, ?)",
              (room_no, capacity, capacity))
    conn.commit()
    conn.close()
    print("✅ Room added successfully!")

def view_rooms():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM rooms")
    for row in c.fetchall():
        print(row)
    conn.close()
