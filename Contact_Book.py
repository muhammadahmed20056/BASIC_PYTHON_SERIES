#Project3
Book=[]
def Add():
    name=str(input("Enter name:"))
    e_mail=str(input("Enter email:"))
    phone_no=int(input("Enter phone number:"))
    Book.append([name,e_mail,phone_no])

def View():
    for book in Book:
        print(book)

def Search():
    name=str(input("Enter name to search:"))
    for book in Book:
        if book[0]==name:
            print(book)
            return
        
        else:
            print("Invalid name...")

def Update():
    name=str(input("Enter name to update:"))
    for book in Book:
        if book[0]==name:
         book[0]=str(input("Enter name:"))
         book[1]=str(input("Enter email:"))
         book[2]=int(input("Enter phone number:"))
         print(book)
         print("Successfully Updated...")
         return
        
        else:
            print("User not found:")

def Delete():
    name=str(input("Enter name to delete:"))
    for book in Book:
        if book[0]==name:
            Book.remove(book)
            return
        
        else:
            print("User not deleted...")


while True:
    print("CONTACT BOOK")
    print("MENU")
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
