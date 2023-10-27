from student import Student
from studyfield import StudyField

class Faculty:
    def __init__(self, ID,name, abbrevation, students, studyFiled):
        self.ID = ID
        self.name = name
        self.abbrevation = abbrevation
        self.students = students
        self.studyFiled = studyFiled
    
    def studentBelongsToThisFaculty(self):
        with open('faculty_data.txt', 'r') as file:
            content = file.readlines()
            belong = False
            for elements in content:
                elementsList = elements.split(" $ ")
                facultyObject = Faculty(elementsList[0],elementsList[1],elementsList[2],elementsList[3],elementsList[4])
                print("ID ",facultyObject.ID," Name ",facultyObject.name)
            facultyID = int(input("Enter faculty id: "))
            studentID = int(input("Enter student id: "))
            elementsList = content[facultyID].split(" $ ")
            facultyObject = Faculty(elementsList[0],elementsList[1],elementsList[2],elementsList[3],elementsList[4])
            for i in eval(facultyObject.students):
                if int(i) == studentID:
                    belong = True
            if belong == True:
                print("Yes")
            else:
                print("No")

    def newFacuty(self):
        with open('faculty_data.txt', 'r') as file:
            content = file.readlines()
            newFacutyID = len(content) 
        newFacutyName = input("Faculty name: ")
        newFacutyAbbrevation = input("Faculty abbrevation: ")
        newFacutyStudents = input("Stuents ID(ex: 1, 23, 41): ")
        newFacutyStudents = "[" + newFacutyStudents + "]"
        newFacutyStudentsList = eval(newFacutyStudents)
        for field, value in StudyField.__dict__.items():
            if not field.startswith("__"):
                print(f"{field} = {value}")
        newFacutyFieldID = input("Chose an ID: ")
        newFacutyObject = Faculty(newFacutyID,newFacutyName,newFacutyAbbrevation,newFacutyStudentsList,newFacutyFieldID)
        newline = str(newFacutyObject.ID) + " $ " + newFacutyObject.name + " $ " + newFacutyObject.abbrevation + " $ " + str(newFacutyObject.students) + " $ " + str(newFacutyObject.studyFiled)
        content.append("\n" + newline)
        with open('faculty_data.txt', 'w') as file:
            for element in content:
                file.write(element)
        print("Faculty was created !!")

    def WhatFacultyStudentBelong(self):
        studentID = int(input("Enter student id: "))
        with open('faculty_data.txt', 'r') as file:
            content = file.readlines()
            belong = False
            for elements in content:
                elementsList = elements.split(" $ ")
                facultyObject = Faculty(elementsList[0],elementsList[1],elementsList[2],elementsList[3],elementsList[4])
                for i in eval(facultyObject.students):
                    if int(i) == studentID:
                        print("Faculty name: "+facultyObject.name)
                        break

    def displayFaculty(self):
        print("Faculty: ")
        with open('faculty_data.txt', 'r') as file:
            content = file.readlines()
            for elements in content:
                elementsList = elements.split(" $ ")
                facultyObject = Faculty(elementsList[0],elementsList[1],elementsList[2],elementsList[3],elementsList[4])
                print(facultyObject.name)
    
    def displayFacultyByField(self):
        for field, value in StudyField.__dict__.items():
            if not field.startswith("__"):
                print(f"{field} = {value}")
        FacutyFieldID = input("Chose an ID: ")
        with open('faculty_data.txt', 'r') as file:
            content = file.readlines()
            print("Faculty: ")
            for elements in content:
                elementsList = elements.split(" $ ")
                facultyObject = Faculty(elementsList[0],elementsList[1],elementsList[2],elementsList[3],elementsList[4])
                if int(facultyObject.studyFiled) == int(FacutyFieldID):
                    print(facultyObject.name)





        