import json

def update_student():
    student_id = input("Enter Student ID to update: ")

    try:
        with open("student_data.json", "r") as file:
            students = json.load(file)

        for student in students:
            if student["id"] == student_id:
                print("\nEnter new details (leave blank to keep existing value):")
                new_name = input(f"New Name ({student['name']}): ") or student["name"]
                new_age = input(f"New Age ({student['age']}): ") or student["age"]
                new_course = input(f"New Course ({student['course']}): ") or student["course"]

                student["name"] = new_name
                student["age"] = new_age
                student["course"] = new_course

                with open("student_data.json", "w") as file:
                    json.dump(students, file, indent=4)

                print("\nStudent record updated successfully!")
                return
        
        print("\nStudent record not found.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo student records found.")
