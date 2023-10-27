from student import Student
from faculty import Faculty
from studyfield import StudyField
faculties = []
students = []
power = True
while power == True:
    print("Options:")
    print("1. Create and assign a student to a faculty")
    print("2. Graduate a student from a faculty.")
    print("3. Display current enrolled students (Graduates would be ignored).")
    print("4. Display graduates (Currently enrolled students would be ignored).")
    print("5. Tell or not if a student belongs to this faculty.")
    print("6. Create a new facult")
    print("7. Search what faculty a student belongs to by a unique identifier (for example by email or a unique ID).")
    print("8. Display University faculties.")
    print("9. Display all faculties belonging to a field. (Ex. FOOD_TECHNOLOGY)")
    print("0.Quit")
    inpt = int(input("Chose one option:"))
    if inpt == 1:
       Student.addstudent
    if inpt == 2:
        studentenFirstName = input("Student first name: ")
        studentenLastName = input("Student last name: ")
        for i in range(0,len(students)):
            if students[i].firstName == studentenFirstName and students[i].lastName == studentenLastName:
                students[i].graduated = True
    if inpt == 3:
        for i in range(0,len(students)):
            if(students[i].graduated == False):
                print(students[i].firstName," ",students[i].lastName)
    if inpt == 4:
        for i in range(0,len(students)):
            if(students[i].graduated == False):
                print(students[i].firstName," ",students[i].lastName)
    if inpt == 5:
        print("Enter the name of a faculty from the list below: ")
        for i in range(0,len(faculties)):
            print(faculties[i].name)
        chosenfaculty = input("chosen faculty: ")
        studentenFirstName = input("Student first name: ")
        studentenLastName = input("Student last name: ")
        for i in range(0,len(students)):
            if faculties[i].name == chosenfaculty:
                for j in range(0,len(faculties[i].students)):
                    if faculties[i].students[i].lastName == studentenLastName and faculties[i].students[i].firstName == studentenFirstName:
                        print("Student blong to the facluty")
                    else:
                        print("Student dosent blong to the facluty")
    if inpt == 6:
        facultyname = input("Facluty name: ")
        facultyabbrevation = input("Facluty abbrevation: ")
        facultystudyfield = input("Facukty study field: ")
        empty = []
        faculties(facultyname,facultyabbrevation,empty,facultystudyfield)

    if inpt == 7:
        print("Enter the name of a faculty from the list below: ")
        for i in range(0,len(faculties)):
            print(faculties[i].name)
        chosenfaculty = input("chosen faculty: ")
        IDorEmail = input("Enter student email or id")
        if "@" in IDorEmail:
            for i in range(0,len(faculties)):
                for j in range(faculties[i].students):
                    if faculties[i].students[j].email == IDorEmail:
                        print(faculties[i])
        else:
            for i in range(0,len(faculties)):
                for j in range(faculties[i].students):
                    if faculties[i].students[j].ID == IDorEmail:
                        print(faculties[i])
    if inpt == 8:
        print("University faculties and its students:")
        for i in range(0,len(faculties)):
            print(faculties[i].name," ",faculties[i].abbrevation)
            for j in range(0,len(faculties[i].students)):
                print(faculties[i].students[j].firstName," ",faculties[i].students[j].lastName)
    if inpt == 0:
        power = False
    
