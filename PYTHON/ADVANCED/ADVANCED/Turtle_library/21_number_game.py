import random

number=1

for i in range(1,22):
    try:
        user=int(input("1,2 or 3:"))
        computer=random.randint(1,3)
        print("user input:")
        for i in range(user):
            print(number)
            if number==21:
                print("you lost")
                break
            number+=1
        print("computer input:")
        for i in range(computer):
            print(number)
            if number==21:
                print("computer lost")
                break 
            number+=1
        player=random.randint(1,3)
        for i in range(player):
            print(number)
            if number==21:
                print("you lost")
                break
            number+=1
    except ValueError:
        print("invalid input, please enter a valid number")    