class Student:
    def __init__(self, ID, firstName, lastName, email, enrollmentData, dataOfBirth, graduated):
        self.ID = ID
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.enrollment_data = enrollmentData
        self.data_of_birth = dataOfBirth
        self.graduated = graduated

    def addstudent(self):
        studentFirstName = input("Student first name: ")
        studentLastName = input("Student last name: ")
        studentEmail = input("Student email: ")
        studentEnrollmentData = input("Student enrollment data: ")
        studentDataOfBirth = input("Student data of birth: ")
        studentGraduated = input("Has the student graduated (True/False): ")
        with open('students_data.txt', 'r') as file:
            content = file.readlines()
            studentID = len(content) 
        studentobject = Student(studentID ,studentFirstName, studentLastName, studentEmail, studentEnrollmentData, studentDataOfBirth, studentGraduated)
        content.append("\n" + str(studentobject.ID) + " $ " + studentobject.first_name + " $ " + studentobject.last_name + " $ " + studentobject.email + " $ " + studentobject.enrollment_data + " $ " + studentobject.data_of_birth + " $ " + studentobject.graduated)
        with open('students_data.txt', 'w') as file:
            for elemet in content:
                file.write(elemet)
        print("Enter the id of a faculty from the list below: ")
        with open('faculty_data.txt', 'r') as file:
            content = file.readlines()
            for txt in content:
                el = txt.split(" $ ")
                print("ID ",el[0]," Name ",el[1])
        chosenfaculty = int(input("chosen faculty: "))
        with open('faculty_data.txt', 'r') as file:
            content = file.readlines()
            i = content[chosenfaculty].split(" $ ")
            IDlist = eval(i[3])
            IDlist.append(int(studentID))
            i[3] = str(IDlist)
            newline = i[0] + " $ " + i[1] + " $ " + i[2] + " $ " + i[3] + " $ " + i[4]
            content[chosenfaculty] = newline
        with open('faculty_data.txt', 'w') as file:
            for elemet in content:
                file.write(elemet)
    
    def graduateAStudent(self):
        studentID = int(input("Enter student id: "))
        with open('students_data.txt', 'r') as file:
            content = file.readlines()
            count = 0
            for i in content:
                ilist = i.split(" $ ")
                if int(ilist[0]) == int(studentID):
                    break
                else:
                    count += 1
            elementList = content[count].split(" $ ")
            studentobject = Student(elementList[0],elementList[1],elementList[2],elementList[3],elementList[4],elementList[5],elementList[6])
            studentobject.graduated = "True"
            newline = str(studentobject.ID) + " $ " + studentobject.first_name + " $ " + studentobject.last_name + " $ " + studentobject.email + " $ " + studentobject.enrollment_data + " $ " + studentobject.data_of_birth + " $ " + studentobject.graduated + "\n" 
            content[count]=newline
        with open('students_data.txt', 'w') as file:
            for element in content:
                file.write(element)
        print("Student was graduates !!")
    
    def displayEnrolled(self):
        print("Enrolled students: ")
        with open('students_data.txt', 'r') as file:
            content = file.readlines()
            for elements in content:
                elementList = elements.strip().split(" $ ")
                if len(elementList) == 7:
                    studentobject = Student(*elementList)
                    if studentobject.graduated == "False":
                        print("ID:", studentobject.ID, "Full name:", studentobject.first_name, studentobject.last_name)

    def displaygraduated(self):
        print("Graduated students: ")
        with open('students_data.txt', 'r') as file:
            content = file.readlines()
            for elements in content:
                elementList = elements.strip().split(" $ ")
                if len(elementList) == 7:
                    studentobject = Student(*elementList)
                    if studentobject.graduated == "True":
                        print("ID:", studentobject.ID, "Full name:", studentobject.first_name, studentobject.last_name)




            
