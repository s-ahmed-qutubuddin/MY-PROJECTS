print("calculator")
while True:
    No1=int(input("Enter number 1"))
    No2=int(input("Enter number 2"))
    print("Press 1 For Addition, Press 2 For Subtraction")
    print("Press 3 For Multipliction, Press 4 for division")
    print("Press 5 For Modulus, Press 6 For Exponent")
    choice1=int(input("Enter your choice"))
    if choice1==1:
        print('Addition=',No1+No2)
    elif choice1==2:
        print("Subtraction=", No1-No2)
    elif choice1==3:
        print("Multiplication=", No1*No2)
    elif choice1==4:
        print("Divison=",No1/No2)
    elif choice1==5:
            print("Modulus=",No1%No2)
    elif choice1==6:
            print("Exponent=",No1**No2)
    else : 
        print("Invalid Choice")
  
12