from student import Student
from faculty import Faculty
from studyfield import StudyField


power = True
while power == True:
    print("Options:")
    print("1. Create and assign a student to a faculty")
    print("2. Graduate a student from a faculty.")
    print("3. Display current enrolled students (Graduates would be ignored).")
    print("4. Display graduates (Currently enrolled students would be ignored).")
    print("5. Tell or not if a student belongs to this faculty.")
    print("6. Create a new faculty")
    print("7. Search what faculty a student belongs to by a unique identifier (for example by email or a unique ID).")
    print("8. Display University faculties.")
    print("9. Display all faculties belonging to a field. (Ex. FOOD_TECHNOLOGY)")
    print("0.Quit")
    inpt = int(input("Chose one option:"))
    if inpt == 1:
        student = Student(None, None, None, None, None, None, None)
        student.addstudent()
        power = False
    if inpt == 2:
        student = Student(None, None, None, None, None, None, None)
        student.graduateAStudent()
        power = False
    if inpt == 3:
        student = Student(None, None, None, None, None, None, None)
        student.displayEnrolled()
        power = False
    if inpt == 4:
        student = Student(None, None, None, None, None, None, None)
        student.displaygraduated()
        power = False
    if inpt == 5:
        faculty = Faculty(None, None, None, None, None)
        faculty.studentBelongsToThisFaculty()
        power = False
    if inpt == 6:
        faculty = Faculty(None, None, None, None, None)
        faculty.newFacuty()
        power = False
    if inpt == 7:
        faculty = Faculty(None, None, None, None, None)
        faculty.WhatFacultyStudentBelong()
        power = False
    if inpt == 8:
        faculty = Faculty(None, None, None, None, None)
        faculty.displayFaculty()
        power = False
    if inpt == 9:
        faculty = Faculty(None, None, None, None, None)
        faculty.displayFacultyByField()
        power = False
    if inpt == 0:
        power = False