#Project5
exp=[]
def Add():
    Expense_name=str(input("Enter a expense name:"))
    amount=int(input("Enter amount:"))
    category=str(input("Enter category type:"))
    exp.append([Expense_name,amount,category])

def View():
    for Exp in exp:
        print(Exp)

def Search():
    exp_name=str(input("Enter a Expense name:"))
    for Exp in exp:
        if Exp[0]==exp_name:
            print(Exp)

def Update():
    exp_name=str(input("Enter a expense name:"))
    for Exp in exp:
        if Exp[0]==exp_name:
            Exp[0]=str(input("Enter a expense name:"))
            Exp[1]=int(input("Enter a amount:"))
            Exp[2]=str(input("Enter a category:"))
            print(Exp)

def Total():
    Total=0
    for Exp in exp:
        Total+=Exp[1]

        print("Total Expense:",Total)

def Delete():
        choice=int(input("Enter a choice:"))
        exp.pop(choice-1)
        print("Expenses deleted..")


while True:
 print("EXPENSE TRACKER")
 print("MENU")
 print("1.ADD")
 print("2.VIEW")
 print("3.SEARCH")
 print("4.UPDATE")
 print("5.TOTAL")
 print("6.DELETE")
 print("7.EXIT")

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
        Total()
 elif choice==6:
    Delete()
 elif choice==7:
      print("Exit Program.....")
      break