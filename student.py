from database import get_connection

# Function to add a new student
def add_student(name, roll_no, department):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO students (name, roll_no, department) VALUES (?, ?, ?)",
            (name, roll_no, department)
        )
        conn.commit()
        print("✅ Student added successfully!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

# Function to view all students
def view_students():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    if students:
        print("\n📋 All Students:")
        print("ID | Name | Roll No | Department")
        print("-" * 35)
        for student in students:
            print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")
    else:
        print("⚠️ No students found.")
    conn.close()
