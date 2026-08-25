#Project4
To_Do=[]
def Add():
    Task=str(input("Enter your task:"))
    To_Do.append([Task,"Pending"])

def View():
    for todo in To_Do:
        print(todo)

def Complete():
    task=int(input("Enter a task no:"))
    To_Do[task-1][1]="Completed"

def Update():
    task=int(input("Enter a task no:"))
    To_Do[task-1][0]=input("Enter task to update:")
    print("Task Updated...")

def Delete():
    task=int(input("Enter task to delete:"))
    To_Do.pop(task-1)
    print("Successfully deleted:")

while True:
 print("TODO  LIST")
 print("MENU")
 print("1.ADD")
 print("2.VIEW")
 print("3.COMPLETE")
 print("4.UPDATE")
 print("5.DELETE")
 print("6.EXIT")

 choice=int(input("Enter a choice:"))
 if choice==1:
        Add()
 elif choice==2:
        View()
 elif choice==3:
        Complete()
 elif choice==4:
        Update()
 elif choice==5:
        Delete()
 elif choice==6:
    print("EXIT PROGRAM...")
    break