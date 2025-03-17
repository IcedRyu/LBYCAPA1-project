import json

def view_students():
    try:
        with open("student_data.json", "r") as file:
            students = json.load(file)
            if not students:
                print("\nNo student records found.")
                return
            print("\nAll Student Records:")
            for student in students:
                print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Current grade: {student['average_grade']}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo student records found.")
