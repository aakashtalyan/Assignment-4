year=int(input("Enter the year you want to check for leap "))
if year%100==0 and year%400==0:
    print("Leap year")
elif year%4==0 and year%100!=0:
    print("Leap year")
else:
    print("Not a leap year")
