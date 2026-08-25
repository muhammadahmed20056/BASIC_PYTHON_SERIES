#Project2
print("\n\t\t\t\t\tSTUDENT RESULT MANAGEMENT SYSTEM")
Student=[]

def Add():
    roll_no=int(input("Enter roll no:"))
    name=str(input("Enter name:"))
    marks=float(input("Enter marks:"))
    Student.append([roll_no,name,marks])
    print("Student Added Successfully...")
    print(Student)

def View():
    for student in Student:
        print(student)

def Search():
    name=str(input("Enter name to search:"))
    for student in Student:
        if student[1]==name:
            print(student)
        else:
            print("Student not exist...")

def Update():
    name_1=str(input("Enter name to update:"))
    for student in Student:
        if student[1]==name_1:
            student[0]=int(input("Enter roll_no:"))
            student[1]=str(input("Enter name:"))
            student[2]=float(input("Enter marks:"))

        print(student)
        print("Update Successfully done.")
    else:
            print("Student not exist..")

def Delete():
    Name_1=str(input("Enter a name:"))
    for student in Student:
     if student[1]==Name_1:
         Student.remove(student)
         print("Successfully Removed!")


while True:
 print("STUDENT RESULT MANAGEMENT SYSTEM...")
 print("MENU:")
 print("1.ADD")
 print("2.VIEW")
 print("3.SEARCH")
 print("4.UPDATE")
 print("5.DELETE")
 print("6.EXIT")
 choice=int(input("Enter a choice:"))
 if choice==1:
  Add()
 elif choice==2: 
  View()
 elif choice==3:
  Search()
 elif choice==4:
   Update()
 elif choice==5:
  Delete()
 elif choice==6:
    print("EXIT PROGRAM...")
    break
 