import random
for i in range(0,10):
    
    a=random.randint(0,9)
    b=random.randint(0,9)
    
    print(a,"*",b,"=")
    
    c=int(input("Enter your answer:"))
    
    if c==a*b:
        print("Right!")
    else:
        print("Wrong.The answer is",a*b)


