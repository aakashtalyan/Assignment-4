m = float(input("Enter your marks ==> "))
n = str(input("enter your name ==> "))
if m<=100 and m>=80:
    print(n,"your grade is ==> A")
elif m<80 and m>=60:
    print(n,"your grade is ==> B")
elif m<60 and m>=50:
    print(n,"your grade is ==> C")
elif m<50 and m>=45:
    print(n,"your grade is ==> D")
elif m<45 and m>=25:
    print(n,"your grade is ==> E")
else:
    print(n,"you failed")
              
    
