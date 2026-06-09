#university management system using oops
class Person:
    university_name="Codegnan University"
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age        
        self.gender=gender
    def display(self):
        pass
    
class Student(Person):
    student_count=0
    def __init__(self,name,age,studentID,depart,year,gender,course):
        super().__init__(name,age,gender)
        self.studentID=studentID
        self.depart=depart
        self.year=year
        self.course=course
        Student.student_count+= 1
        
    def display(self):
        print("--------Student Details-------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.depart}")
        print(f"Gender: {self.gender}")
        print(f"StudentID: {self.studentID}")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")
        
std=Student("Neha",21,"CSE","Female",45678,"AI&ML","4th year")
std.display()

class Faculty(Person):
    faculty_count=0
    def __init__(self,name,age,depart,gender,facultyID,education):
        super().__init__(name,age,gender)
        self.facultyID=facultyID
        self.depart=depart
        self.education=education
        Faculty.faculty_count+=1
    def display(self):
        print("-------Faculty Details-------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.depart}")
        print(f"Gender: {self.gender}")
        print(f"Faculty ID: {self.facultyID}")
        print(f"Education: {self.education}")
fac=Faculty("Ram",45,"CSE","MALE","TGH456","MTech")
fac.display()

class Watchman(Person):
    watchman=0
    def __init__(self,name,age,gender,ID):
        super().__init__(name,age,gender)                
        self.ID=ID
        Watchman.watchman+=1
    def display(self):
        print("-------WatchMan Details--------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")        
        print(f"Gender: {self.gender}")
        print(f"WatchMan ID: {self.ID}")
watch=Watchman("Raju",67,"Female","HTD98567")
watch.display()

class Helper(Person):
    helper=0
    def __init__(self,name,age,gender,ID):
        super().__init__(name,age,gender)                
        self.ID=ID
        Helper.helper+=1
    def display(self):
        print("-------Helper Details--------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")        
        print(f"Gender: {self.gender}")
        print(f"Helper ID: {self.ID}")
h=Helper("Roja",50,"Female","GHT87654")
h.display()

class Driver(Person):
    driver=0
    def __init__(self,name,age,gender,ID,Salary):
        super().__init__(name,age,gender)                
        self.ID=ID
        self.Salary=Salary
        Driver.driver+=1
    def display(self):
        print("-------Driver Details--------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")        
        print(f"Gender: {self.gender}")
        print(f"Driver ID: {self.ID}")
        print(f"Salary: {self.Salary}")
d=Driver("Krishna",56,"Male","IKF78654",30000)
d.display()

class labassistance(Person):
    lab=0
    def __init__(self,name,age,gender,education,ID):
        super().__init__(name,age,gender)
        self.education=education
        self.ID=ID
        labassistance.lab+=1
    def display(self):
        print("-------labassistance--------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")        
        print(f"Gender: {self.gender}")
        print(f"Lab Assistance ID: {self.ID}")
        print(f"Education: {self.education}")
l=labassistance("Prema",24,"FEMALE",897654,"BTech")
l.display()

class Non_teaching(Person):
    non=0
    def __init__(self,name,age,gender,education,ID):
        super().__init__(name,age,gender)
        self.education=education
        self.ID=ID
        Non_teaching.non+=1
    def display(self):
        print("-------Non Teaching Staff--------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")        
        print(f"Gender: {self.gender}")
        print(f"Lab Assistance ID: {self.ID}")
        print(f"Education: {self.education}")
n=Non_teaching("Krishna",45,"MALE",67543,"BTech")
n.display()
           
print("---------Total Counts------------")
print("Total Students",Student.student_count)
print("Total Faculty",Faculty.faculty_count)
print("Total Watchman",Watchman.watchman)
print("Total Helpers",Helper.helper)
print("Total Drivers",Driver.driver)
print("Total Labassistance",labassistance.lab)
print("Total NON-Teaching Staff",Non_teaching.non)
