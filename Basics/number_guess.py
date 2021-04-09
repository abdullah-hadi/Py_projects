import random

number = random.randint(1,50)

user_in= int(input("Guess a number between 1 and 50: "))

while True:
    if user_in==number:
        print(f"\ncongratulations! you won!!\nthe number is {number}\n")
        quit()
    else:
        if user_in>number:
            user_in=int(input("\nguess a smaller number! : "))

        else:
            user_in=int(input("\nguess a bigger number! : "))
