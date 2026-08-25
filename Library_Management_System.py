#Project7
Books=[]
def Add():
    id=int(input("Enter id of Book:"))
    name=str(input("Enter a name of book:"))
    author=str(input("Enter a aurther name:"))
    books={
        "id":id,
        "name":name,
         "author":author,
         "Status":"Available"
    }
    Books.append(books)
    print("Book Successfully Added!")
    return

def View():
    for books in Books:
        print(books)
        return

def Search():
    id=(int(input("Enter a id:")))
    for books in Books:
     if books["id"]==id:
      print(books)
      return

    else:
     print("Book not found...")

def Update():
   id=int(input("Enter a id to update:"))
   for books in Books:
      if books["id"]==id:
         books["id"]=int(input("Enter a new id:"))
         books["name"]=str(input("Enter a new name:"))
         books["author"]=str(input("Enter a new author name:"))
         print(books)
         print("Books Successfully Added!")
         return

      else:
         print("Book not updated!")

def Delete():
   id=int(input("Enter a id to delete:"))
   for books in Books:
      if books["id"]==id:
         Books.remove(books)
         print("Successfully Deleted!")
         return

      else:
         print("Not Deleted...")
         
def Issue():
   id=int(input("Enter a id to see the book status:"))
   for books in Books:
      if books["id"]==id:
         if books["Status"]=="Available":
            books["Status"]="Issued"
            print(books)
            print("Book is issued Successfully!")
      else:
            print("Book is already issued...")
            return
print("Book doesnot exist!")

def Return():
   id=int(input("Enter a id to return a book:"))
   for books in Books:
      if books["id"]==id:
       if books["Status"]=="Issued":
         books["Status"]="Available"
         print(books)
         print("Book Successfully return!")
       else:
          print("Book not return")
          return
print("Book doesnot exist...")

while True:
   print("LIBRARY MANAGEMENT SYSTEM:")
   print("MENU")
   print("1.ADD")
   print("2.VIEW")
   print("3.SEARCH")
   print("4.UPDATE")
   print("5.DELETE")
   print("6.ISSUE")
   print("7.RETURN")
   print("8.EXIT")
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
        Issue()
   elif choice==7:
        Return()
   elif choice==8:
      print("Exit Program...")
   else:
      print("Invalid Number Enter...")
      break