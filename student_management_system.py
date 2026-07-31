class Student:
    def __init__(self):
        self.student_information = []

    #Create
    def create_student_details(self):
        NoOfStudents = int(input("\nEnter no of students: "))

        for p in range(NoOfStudents):
            self.student_information.append({})

        for i in range(NoOfStudents):
            name = input("\nEnter student name: ")
            
            while 1:
                roll_no = int(input("Enter roll_no: "))
                for roll in range(i):
                    if self.student_information[roll]["Roll_no"] == roll_no:
                        print("Roll no already exist enter another roll number")
                        break
                else: 
                    self.student_information[i]["Roll_no"] = roll_no
                    break
            self.student_information[i]["Name"] = name
            clas = input("Enter class of student: ").lower()
            self.student_information[i]["Class"] = clas
            self.student_information[i]["marks"] = {}
            s = int(input("Enter no of subjects for this student: "))

            for j in range(s):
                self.subjects = input(f"Enter subject{j+1}_name: ").lower()
                self.marks = float(input(f"Enter marks of subject{j+1}_name: "))
                self.student_information[i]["marks"][self.subjects] = self.marks

            total_marks = 0

            for k in self.student_information[i]["marks"].values():
                total_marks += k

            average = float(total_marks)/len(self.student_information[i]["marks"])
            self.student_information[i]["average"] = float(f"{average:.2f}")

            if average >= 90:
                self.student_information[i]["grade"] = "A+"
            elif average >= 80:
                self.student_information[i]["grade"] = "A"
            elif average >= 70:
                self.student_information[i]["grade"] = "B+"
            elif average >= 60:
                self.student_information[i]["grade"] = "B"
            elif average >= 50:
                self.student_information[i]["grade"] = "C"
            elif average >= 40:
                self.student_information[i]["grade"] = "D"
            else:
                self.student_information[i]["grade"] = "E"
                
            
    
    #Read
    def read_student_details(self):

        print("=== Here are Student's Details ===")
        for i in range(len(self.student_information)):
            print(f"\n{self.student_information[i]}")

    #Update
    def update_student_details(self):

        while 1:
            m = int(input("\nEnter roll no of that student where you want to update marks: "))
            q = input("Enter subject name for updation: ").lower()
            r = float(input("Enter updated marks: "))

            for i in range(len(self.student_information)):
                if(m == self.student_information[i]["Roll_no"]):
                    self.student_information[i]["marks"][q] = r
                    total_marks = 0
                                    
                    for k in self.student_information[i]["marks"].values():
                        total_marks += k
                    
                    average = float(total_marks)/len(self.student_information[i]["marks"])
                    self.student_information[i]["average"] = float(f"{average:.2f}")
                    
                    if average >= 90:
                        self.student_information[i]["grade"] = "A+"
                    elif average >= 80:
                        self.student_information[i]["grade"] = "A"
                    elif average >= 70:
                        self.student_information[i]["grade"] = "B+"
                    elif average >= 60:
                        self.student_information[i]["grade"] = "B"
                    elif average >= 50:
                        self.student_information[i]["grade"] = "C"
                    elif average >= 40 :
                        self.student_information[i]["grade"] = "D"
                    else:
                        self.student_information[i]["grade"] = "E"
                    print("Updated successfully")
                    break
                
            else:
                print("Student with this roll_no not exist")
            
            f = input("Want to update more students? yes/no ")

            if f.upper() == "NO":
                break
        print("=== Here are Student's details after updation ===")
        for j in range(len(self.student_information)):
            print(f"\n{self.student_information[j]}")

    #Delete
    def delete_Student_details(self):
        while 1:
            u = int(input("\nEnter roll no of that student where you want to delete student: "))
            for i in range(len(self.student_information)):
                if self.student_information[i]["Roll_no"] == u:
                    self.student_information.pop(i)
                    print("Student deleted successfully")
                    break
            else:
                print("Student with this roll_no not exist")

            t = input("Do you want to delete more students? yes/no ")
            if t.lower() == "no":
                break

        print("=== Here are Students's details after deletion ===")
        for j in range(len(self.student_information)):
            print(f"\n{self.student_information[j]}")
            


s1 = Student()

s1.create_student_details()

print("1) See student details")
print("2) Update student details")
print("3) Delete student details")
print("4) Exit")

while 1:
    q = int(input("Enter choice: "))
    if q == 1:
        s1.read_student_details()
    elif q == 2:
        s1.update_student_details()
    elif q == 3:
        s1.delete_student_details()
    elif q == 4:
        break