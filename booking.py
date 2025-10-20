from database import get_connection

def book_room(student_id, room_no):
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT available FROM rooms WHERE room_no=?", (room_no,))
    room = c.fetchone()

    if not room:
        print("❌ Room not found!")
        return

    available = room[0]
    if available > 0:
        c.execute("INSERT INTO bookings (student_id, room_no) VALUES (?, ?)", (student_id, room_no))
        c.execute("UPDATE rooms SET available = available - 1 WHERE room_no=?", (room_no,))
        conn.commit()
        print("✅ Room booked successfully!")
    else:
        print("❌ No beds available in this room.")
    conn.close()

def view_bookings():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''SELECT b.booking_id, s.name, r.room_no
                 FROM bookings b
                 JOIN students s ON b.student_id = s.id
                 JOIN rooms r ON b.room_no = r.room_no''')
    for row in c.fetchall():
        print(row)
    conn.close()
