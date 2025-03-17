import json

def search_student():
    student_id = input("Enter Student ID to search: ")

    try:
        with open("student_data.json", "r") as file:
            students = json.load(file)
            for student in students:
                if student["id"] == student_id:
                    print(f"\nStudent Found:\nID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
                    return
            print("\nStudent record not found.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo student records found.")
