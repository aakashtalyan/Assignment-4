candy=int(input("Enter the number if candies in the bowl "))
if candy<=200:
    for i in range(0,201):
        if i%5==2 and i%6==3 and i%7==2:
            print("Number of candies:",i)
            if(candy==i):
                print("You win all candies")
            else:
                print("You are wrong!!\nNo of candies in the bowl are",i)
            
else:
    print("Candies are not greater than 200")