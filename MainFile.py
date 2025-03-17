import add_student
import view_students
import search_student
import update_student
import remove_student

def main_menu():
    while True:
        print("\nStudent Tracking System")
        print("1. Add Student Record")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Record")
        print("5. Remove Student Record")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_student.add_student()
        elif choice == "2":
            view_students.view_students()
        elif choice == "3":
            search_student.search_student()
        elif choice == "4":
            update_student.update_student()
        elif choice == "5":
            remove_student.remove_student()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
