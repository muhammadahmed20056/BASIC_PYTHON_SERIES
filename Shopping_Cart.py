#Project6
cart=[]
def Add():
    product_name=str(input("Enter a Product name:"))
    price=int(input("Enter a Price:"))
    quantity=int(input("Enter a quantity:"))
    cart.append([product_name,price,quantity])

def View():
    for Cart in cart:
        print(Cart)

def Update():
    name=str(input("Enter a product name:"))
    for Cart in cart:
        if Cart[0]==name:
            Cart[0]=str(input("Enter a new product name:"))
            Cart[1]=int(input("Enter a new amount:"))
            Cart[2]=int(input("Enter a new quantity:"))

def Total():
    Total=0
    for Cart in cart:
        Total+=Cart[1]*Cart[2]
        print("Total Price:",Total)

def Delete():
    product_no=int(input("Enter a Product number:"))
    cart.pop(product_no-1)

while True:
 print("SHOPPING CART:")
 print("MENU")
 print("1.ADD")
 print("2.VIEW")
 print("3.UPDATE")
 print("4.TOTAL")
 print("5.DELETE")
 print("6.EXIT")

 choice=int(input("Enter a choice:"))
 if choice==1:
        Add()
 elif choice==2:
        View()
 elif choice==3:
        Update()
 elif choice==4:
        Total()
 elif choice==5:
        Delete()
 elif choice==6:
      print("Exit Program.....")
      break