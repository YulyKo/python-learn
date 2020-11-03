# Розробити клас Student, який буде містити 
# елементи для зберігання: ім'я, вік, стать, телефон. 
# Написати ф-ї члени, які зможуть змінювати їх індивідуально. 
# Написати ф-ю, яка буде виводити всю інформацію форматовано..

class Student:
    def __init__(self):
        pass

    def getDataOfStudent(self):
        self.getNameFromUser()
        self.getAgeFromUser()
        self.getSexFromUser()
        self.getPhoneFromUser()
        pass

    def getNameFromUser(self):
        print("Input name: ")
        self.__setName(input())
        pass

    def getSexFromUser(self):
        print("Input sex: ")
        self.__setSex(input())
        pass

    def getAgeFromUser(self):
        print("Input age: ")
        self.__setAge(input())
        pass

    def getPhoneFromUser(self):
        print("Input phone: ")
        self.__setPhone(input())
        pass

    def __setName(self, name):
        self.name = name
        pass

    def __setSex(self, sex):
        self.sex = sex
        pass

    def __setAge(self, age):
        self.age = age
        pass

    def __setPhone(self, phone):
        self.phone = phone
        pass
    def getName(self, name):
        return self.name 

    def getSex(self, sex):
        return self.sex

    def getAge(self, age):
        return self.age

    def getPhone(self, phone):
        return self.phone

class StudentsList:
    def __init__(self):
        self.StudentsList = []
        pass

    def addStudentToList(self, studentData):
        self.StudentsList.append(studentData)
        pass

    def getStudentList(self):
        for student in self.StudentsList:
            print("name: " + student.name + " | sex: " + student.sex + 
            " | age:  " + str(student.age) + " | phone:  " + student.phone + "\n-----------") 
        pass
    
    def deleteStudentFromList(self, phone):
        for student in range(0, len(self.StudentsList), 1):
            if self.StudentsList[student].phone == phone:
                self.StudentsList.pop(student)
                pass
            pass
        pass

    def updateStudentData(self, oldPhone, newStudentData):
        # 

        for index in range(0, len(self.StudentsList), 1):
            if self.StudentsList[index].phone == oldPhone:
                self.StudentsList[index].name = newStudentData.name
                self.StudentsList[index].age = newStudentData.age
                self.StudentsList[index].sex = newStudentData.sex
                self.StudentsList[index].phone = newStudentData.phone
            pass
        pass
pass

StudentsList = StudentsList()

while True:
    print("\nWelcome to menu of Student Book \n *-*-*-*-*-*-*-*-*-*-*-*-*\n")
    print("Chouse action:\n1. Add student\n2. Watch student book\n3. Delete Student by phone\n4. Update student data")
    actionId = int(input())
    if actionId == 1:
        newStudent = Student()
        newStudent.getDataOfStudent()
        StudentsList.addStudentToList(newStudent)
    if actionId == 2:
        StudentsList.getStudentList()
    if actionId == 3:
        print("Input phone:")
        phone = input()
        StudentsList.deleteStudentFromList(phone)
    if actionId == 4:
        print('Input phone: ')
        oldPhone = input()
        newStudentData = Student()
        newStudentData.getDataOfStudent()
        StudentsList.updateStudentData(oldPhone, newStudentData)
    if actionId >= 5:
        break
