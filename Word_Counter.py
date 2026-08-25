#Project10
text=""
def Add():
    global text
    text=str(input("Enter a sentence:"))
    print(text)

def Words():
    word=len(text.split())
    print(word)

def character():
    character=len(text)
    print(character)

def Space():
    space=text.count(" ")
    print(space)


def Remove():
    space=text.replace(" ","")
    print(space)

while True:
 print("WORD COUNTER")
 print("MENU")
 print("1.ADD")
 print("2.WORD")
 print("3.CHARACTER")
 print("4.SPACE")
 print("5.REMOVE")
 print("6.EXIT")
 choice=int(input("Enter a choice:"))
 if choice==1:
     Add()
 elif choice==2:
     Words()
 elif choice==3:
     character()
 elif choice==4:
     Space()
 elif choice==5:
     Remove()
 elif choice==6:
     print("EXIT PROGRAM...")
     break 
