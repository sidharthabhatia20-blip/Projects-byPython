import sqlite3
import os

dp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student.db")
db = sqlite3.connect(dp)
cur = db.cursor()

class Student:
    def __init__(self):
        self.student_information = []

    #Create
    def create_student_details(self):
        NoOfStudents = int(input("\nEnter no of students: "))

        sql_command = """CREATE TABLE IF NOT EXISTS STUDENTS(ROLL_NO INTEGER PRIMARY KEY, NAME TEXT, 
        CLASS TEXT, Total_MARKS DECIMAL, Average DECIMAL(4, 2), GRADE CHAR(5))"""
        cur.execute(sql_command)
        db.commit()
        
        st_marks = """CREATE TABLE IF NOT EXISTS MARK(ROLL_NO INTEGER, SUBJECT TEXT, 
        MARKS DECIMAL(4, 2), PRIMARY KEY(ROLL_NO, SUBJECT))"""
        cur.execute(st_marks)
        db.commit()

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
                    cur.execute("select ROLL_NO FROM students where ROLL_NO = ?", (roll_no,))

                    if cur.fetchone() is not None:
                        print("Roll no already stored in main database enter another one")
                        continue

                    self.student_information[i]["Roll_no"] = roll_no
                    break
            self.student_information[i]["Name"] = name
            clas = input("Enter class of student: ").lower()
            self.student_information[i]["Class"] = clas
            
            self.student_information[i]["marks"] = {}
            s = int(input("Enter no of subjects for this student: "))

            vs = 0
            while vs < s:
                self.subjects = input(f"Enter subject {vs+1} name: ").lower
                sub = cur.execute("select ROLL_NO, SUBJECT FROM MARK WHERE SUBJECT = ? AND ROLL_NO = ?", (self.subjects, roll_no))
                if sub.fetchone() is not None:
                    print("This subject already exist enter another subject")
                    continue
                else:
                    self.marks = float(input(f"Enter {vs+1} marks: "))
                    cur.execute("insert into MARK(ROLL_NO, SUBJECT, MARKS) VALUES(?, ?, ?)", (roll_no, self.subjects, self.marks))
                    db.comit()
                    self.student_information[i]["marks"][self.subjects] = self.marks
                    vs = vs+1
                    
            
            total_marks = 0

            for k in self.student_information[i]["marks"].values():
                total_marks += k

            average = round((total_marks)/len(self.student_information[i]["marks"]), 2)
            
            self.student_information[i]["average"] = float(f"{average:.2f}")

            grade = ''
            if average >= 90:
                grade = 'A+'
                self.student_information[i]["grade"] = "A+"
            elif average >= 80:
                grade = 'A'
                self.student_information[i]["grade"] = "A"
            elif average >= 70:
                grade = 'B+'
                self.student_information[i]["grade"] = "B+"
            elif average >= 60:
                grade = 'B'
                self.student_information[i]["grade"] = "B"
            elif average >= 50:
                grade = 'C'
                self.student_information[i]["grade"] = "C"
            elif average >= 40:
                grade = 'D'
                self.student_information[i]["grade"] = "D"
            else:
                grade = 'E'
                self.student_information[i]["grade"] = "E"
            cur.execute("""INSERT INTO STUDENTS(ROLL_NO, NAME, CLASS, TOTAL_MARKS, AVERAGE, GRADE)
            VALUES(?, ?, ?, ?, ?, ?)""", (roll_no, name, clas, total_marks, average, grade))

            db.commit()
                
            
    
    #Read
    def read_student_details(self):

        cur.execute("select Students.ROLL_NO, Students.NAME, Students.CLASS, MARK.SUBJECT, MARK.MARKS, STUDENTS.TOTAL_MARKS, STUDENTS.AVERAGE, STUDENTS.GRADE from students JOIN MARK ON STUDENTS.ROLL_NO = MARK.ROLL_NO order by STUDENTS.ROLL_NO ASC")
        data = cur.fetchall()
        
        print("=== Here are Student's Details ===")

        print(f"\nRollno\tName\tClass\tSubject\tMarks\tTotal Marks\tAverage\tGrade")
        for row in data:
            print(f"\n{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]:.2f}\t{row[7]}")


    #Update
    
    def update_student_details(self):

        while 1:
            m = int(input("\nEnter roll no of that student where you want to update marks: "))

            # Check whether student exists in database
            cur.execute("SELECT ROLL_NO FROM STUDENTS WHERE ROLL_NO = ?", (m,))

            if cur.fetchone() is None:
                print("Student with this roll_no not exist")

            else:
                q = input("Enter subject name for updation: ").lower()
                r = float(input("Enter updated marks: "))

                # Check whether subject exists for this student
                cur.execute(
                    "SELECT MARKS FROM MARK WHERE ROLL_NO = ? AND SUBJECT = ?",
                    (m, q)
                )

                if cur.fetchone() is None:
                    print("This subject does not exist for this student")

                else:
                    # Update marks in MARK table
                    cur.execute(
                        "UPDATE MARK SET MARKS = ? WHERE ROLL_NO = ? AND SUBJECT = ?",
                        (r, m, q)
                    )
                    db.commit()

                    # Get all updated marks from database
                    cur.execute(
                        "SELECT MARKS FROM MARK WHERE ROLL_NO = ?",
                        (m,)
                    )

                    marks_data = cur.fetchall()

                    total_marks = 0

                    for k in marks_data:
                        total_marks += k[0]

                    average = round(total_marks / len(marks_data), 2)

                    # Calculate grade
                    if average >= 90:
                        g = "A+"
                    elif average >= 80:
                        g = "A"
                    elif average >= 70:
                        g = "B+"
                    elif average >= 60:
                        g = "B"
                    elif average >= 50:
                        g = "C"
                    elif average >= 40:
                        g = "D"
                    else:
                        g = "E"

                    # Update STUDENTS table
                    cur.execute(
                        """UPDATE STUDENTS
                        SET TOTAL_MARKS = ?, AVERAGE = ?, GRADE = ?
                        WHERE ROLL_NO = ?""",
                        (total_marks, average, g, m)
                    )
                    db.commit()

                    print("Updated successfully")

            f = input("Want to update more students? yes/no: ")

            if f.upper() == "NO":
                break

    #Delete
    def delete_Student_details(self):
        while 1:
            u = int(input("\nEnter roll no of that student where you want to delete student: "))
            cur.execute("select roll_no from students where roll_no = ?", (u,))
            if cur.fetchone() is not None:
                cur.execute("Delete from students where roll_no = ?", (u,))
                db.commit()
                
                cur.execute("Delete from mark where roll_no = ?", (u,))
                db.commit()
                
                for i in range(len(self.student_information)):
                    if self.student_information[i]["Roll_no"] == u:
                        self.student_information.pop(i)
                        break
                print("Student deleted successfully")
            else:
                print("Student with this roll no not exist")
            t = input("Do you want to delete more students? yes/no: ")
            
            if t.lower() == "no":
                break
        print("=== Here are Student's details after deletion ===")
        
        for j in range(len(self.student_information)):
            print(f"\n{self.student_information[j]}")
            


s1 = Student()

s1.create_student_details()

print("1) See student details")
print("2) Update student details")
print("3) Delete student details")
print("4) Exit")


while 1:
    q = int(input("\nEnter choice: "))
    if q == 1:
        s1.read_student_details()
    elif q == 2:
        s1.update_student_details()
    elif q == 3:
        s1.delete_Student_details()
    elif q == 4:
        break
db.close()