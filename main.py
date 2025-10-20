from database import setup_database
from student import add_student, view_students
from room import add_room, view_rooms
from booking import book_room, view_bookings

def menu():
    print("\n🏨 Hostel Booking System")
    print("1. Add Student")
    print("2. Add Room")
    print("3. View Students")
    print("4. View Rooms")
    print("5. Book Room")
    print("6. View Bookings")
    print("7. Exit")

def main():
    # Setup database and tables
    setup_database()

    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == '1':
            name = input("Enter student name: ").strip()
            roll = input("Enter roll no: ").strip()
            dept = input("Enter department: ").strip()
            if name and roll and dept:
                add_student(name, roll, dept)
            else:
                print("❌ All fields are required!")

        elif choice == '2':
            try:
                rno = int(input("Enter room number: "))
                cap = int(input("Enter capacity: "))
                if cap > 0:
                    add_room(rno, cap)
                else:
                    print("❌ Capacity must be greater than 0.")
            except ValueError:
                print("❌ Room number and capacity must be integers.")

        elif choice == '3':
            view_students()

        elif choice == '4':
            view_rooms()

        elif choice == '5':
            try:
                sid = int(input("Enter student ID: "))
                rno = int(input("Enter room number: "))
                book_room(sid, rno)
            except ValueError:
                print("❌ Student ID and Room number must be integers.")

        elif choice == '6':
            view_bookings()

        elif choice == '7':
            print("Exiting... 👋")
            break

        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
