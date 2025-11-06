import time
class Students:

    def __init__(self, *args):
        self.studentList = [*args]

    def addStudent(self, name):
        self.studentList.append(name)

    def removeStudent(self, name):
        try:
            self.studentList.remove(name)
        except:
            print("Please enter existing name in the list")

    def showStudents(self):
        print(f"Current student list: {self.studentList} ")

students = Students("ahmet", "ayşe", "eren")   
print("Welcome! You can add and remove Students here")
students.showStudents()

while True:
    time.sleep(1)
    print("--------------")
    print("What do you want?")
    choice = input("Choose a number in (0, 1, 2, 3) (Exit/ Add Student/ Remove Student/ Show Current Students)")

    try:
        if int(choice) not in [0, 1, 2, 3]:
            print("Please choose a number in 0/1/2/3!")
            continue
    except:
        print("Please choose a number in 0/1/2/3!")
        continue

    if int(choice) == 0:
        print("Exiting from program...")
        break
    elif int(choice) == 1:
        studentName = input("Enter Student name to add:")
        students.addStudent(studentName)
        print("Student added")
        continue
    elif int(choice) == 2:
        studentName = input("Enter Student name to remove:")
        students.addStudent(studentName)
        print("Student removed")
        continue
    elif int(choice) == 3:
        students.showStudents()
        continue
