#Project1
print("\n\t\t\t\t\tGRADING CALCULATOR")
sub_1=float(input("Enter maths number:"))
sub_2=float(input("Enter urdu number:"))
sub_3=float(input("Enter islamiat number:"))
sub_4=float(input("Enter chemistry number:"))
sub_5=float(input("Enter physics number:"))
sub_6=float(input("Enter biology number:"))
sub_7=float(input("Enter computer number:"))
sub_8=float(input("Enter english number:"))
sub_9=float(input("Enter pst number:"))
sub_10=float(input("Enter sindhi number:"))

sum=sub_1+sub_2+sub_3+sub_4+sub_5+sub_6+sub_7+sub_8+sub_9+sub_10
print("Total Sum of Subjects is:",sum)
percentage=(sum/1000)*100
print("Your Percentage is:",percentage)
if percentage>=90 and percentage<=100:
    print("GRADE:A+")
elif percentage>=80 and percentage<90:
    print("GRADE:A")
elif percentage>=70 and percentage<80:
    print("GRADE:B")   
elif percentage>=60 and percentage<70:
    print("GRADE:C")
elif percentage>=50 and percentage<60:
    print("GRADE:D")
elif percentage>=40 and percentage<50:
    print("GRADE:F")
else:
    print("BELOW 40%..NEED MORE IMPROVEMENT!")
    