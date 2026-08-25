#Project8
Account=[]
def create():
    Acc_no=int(input("Enter a account number:"))
    name=str(input("Enter a name:"))
    balance=int(input("Enter a balance:"))
    account={
        "Acc_no":Acc_no,
        "name":name,
        "balance":balance
    }
    Account.append(account)
    print("Successfully Added...")
    return
    
def View():
    for account in Account:
        print(account)

def Search():
    no=int(input("Enter a Account number to search:"))
    for account in Account:
        if account["Acc_no"]==no:
            print(account)
        else:
            print("Account not found:")
            return

def deposit():
    no=int(input("Enter a Account number to deposit amount:"))
    for account in Account:
        if account["Acc_no"]==no:
            deposit=float(input("Enter a deposit:"))
            account["balance"]+=deposit
            print("Deposit Successfully Added!")
        else:
            print("Account not found!")

def Withdraw():
    no=int(input("Enter a Account number to withdraw:"))
    for account in Account:
        if account["Acc_no"]==no:
            withdraw=float(input("Enter a withdraw amount:"))
            account["balance"]-=withdraw
            print("Withdraw Successfully!")

def check():
    no=int(input("Enter a Account number to check balance:"))
    for account in Account:
        if account["Acc_no"]==no:
            print("Balance:",account["balance"])

def Delete():
    no=int(input("Enter a Account number to delete:"))
    for account in Account:
        if account["Acc_no"]==no:
            Account.remove(account)
            print("Account Removed!")
while True:
 print("BANKING ACCOUNT SYSTEM...")
 print("MENU")
 print("1.CREATE")
 print("2.VIEW")
 print("3.SEARCH")
 print("4.DEPOSIT")
 print("5.WITHDRAW")
 print("6.CHECK")
 print("7.DELETE")
 print("8.EXIT")
 choice=int(input("Enter a choice:"))
 if choice==1:
  create()
 elif choice==2:
  View()
 elif choice==3:
  Search()
 elif choice==4:
  deposit()
 elif choice==5:
  Withdraw()
 elif choice==6:
  check()
 elif choice==7:
  Delete()
 elif choice==8:
    print("Exit Program...")
    break
 