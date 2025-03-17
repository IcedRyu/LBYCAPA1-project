import json

def add_student():
    student = {}
    student["id"] = input("Enter Student ID: ")
    student["name"] = input("Enter Student Name: ")
    student["age"] = input("Enter Student Age: ")
    student["course"] = input("Enter Course: ")

    # Add grades input for each category
    student["practical_exam_1"] = float(input("Enter Practical Exam 1 Grade (15%): "))
    student["practical_exam_2"] = float(input("Enter Practical Exam 2 Grade (15%): "))
    student["lab_exercises"] = float(input("Enter Lab Exercises Grade (40%): "))
    student["lab_activities"] = float(input("Enter Lab Activities Grade (10%): "))
    student["final_project"] = float(input("Enter Final Project Grade (15%): "))
    student["teacher_evaluation"] = float(input("Enter Teacher Evaluation Grade (5%): "))

    # Calculate average grade based on weighted percentages
    average_grade = (
        student["practical_exam_1"] * 0.15 +
        student["practical_exam_2"] * 0.15 +
        student["lab_exercises"] * 0.40 +
        student["lab_activities"] * 0.10 +
        student["final_project"] * 0.15 +
        student["teacher_evaluation"] * 0.05
    )

    student["average_grade"] = round(average_grade, 2)  # Round the average to 2 decimal places

    # Try to open the file and read the existing student data, or create an empty list if the file doesn't exist
    try:
        with open("student_data.json", "r") as file:
            students = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []

    # Add the new student to the list
    students.append(student)

    # Write the updated student data back to the file
    with open("student_data.json", "w") as file:
        json.dump(students, file, indent=4)


