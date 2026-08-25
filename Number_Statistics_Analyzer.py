#Project9
list=[]
def Add():
    n=int(input("Enter a choice to enter total no:"))
    for i in range(n):
        number=int(input("Enter a number:"))
        list.append(number)

def View():
    for number in list:
        print(number)

def Total():
    total=0

    for number in list:
        total+=number


        print(total)

def Average():
     total=0
    
     for number in list:
            total+=number
            Average=total/len(list)


     print("Average:",Average)

def Maximum():
     print("Maximum:",max(list))

def Minimum():
     print("Minimum:",min(list))

while True:
 print("NUMBER STATISTICS ANALYZER")
 print("MENU")
 print("1.ADD")
 print("2.VIEW")
 print("3.TOTAL")
 print("4.AVERAGE")
 print("5.MAXIMUM")
 print("6.MINIMUM")
 print("7.EXIT")
 choice=int(input("Enter your choice:"))
 if choice==1:
     Add()
 elif choice==2:
     View()
 elif choice==3:
     Total()
 elif choice==4:
     Average()
 elif choice==5:
     Maximum()
 elif choice==6:
     Minimum()
 elif choice==7:
     print("Exit Porgram...")
     break
 else:
     print("Invalid choice:")

