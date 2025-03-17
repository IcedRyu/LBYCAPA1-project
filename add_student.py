import json

def add_student():
    student = {}
    student["id"] = input("Enter Student ID: ")
    student["name"] = input("Enter Student Name: ")
    student["age"] = input("Enter Student Age: ")
    student["course"] = input("Enter Course: ")

    try:
        with open("student_data.json", "r") as file:
            students = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []

    students.append(student)

    with open("student_data.json", "w") as file:
        json.dump(students, file, indent=4)

    print("\nStudent record added successfully!")
