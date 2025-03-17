import json

def remove_student():
    student_id = input("Enter Student ID to remove: ")

    try:
        with open("student_data.json", "r") as file:
            students = json.load(file)

        updated_students = [student for student in students if student["id"] != student_id]

        if len(updated_students) == len(students):
            print("\nStudent record not found.")
            return

        with open("student_data.json", "w") as file:
            json.dump(updated_students, file, indent=4)

        print("\nStudent record removed successfully!")

    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo student records found.")
